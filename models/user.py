from tortoise import fields
from tortoise.models import Model
import uuid


class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, unique=True)
    referral_code = fields.CharField(max_length=36, unique=True)
    referral_count = fields.IntField(default=0)
    referred_by = fields.ForeignKeyField("models.User", related_name="referrals", null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

    @classmethod
    async def generate_unique_referral_code(cls):
        while True:
            referral_code = str(uuid.uuid4())
            if not await cls.filter(referral_code=referral_code).exists():
                return referral_code




async def add_user(tg_id: int, full_name: str, username: str, referred_by_code: str = None):
    referral_code = await User.generate_unique_referral_code()

    user = User(
        tg_id=tg_id,
        full_name=full_name,
        username=username,
        referral_code=referral_code,
        referred_by=None
    )

    if referred_by_code:
        referrer = await User.get_or_none(referral_code=referred_by_code)
        if referrer:
            user.referred_by = referrer
            referrer.referral_count += 1
            await referrer.save()

    await user.save()
