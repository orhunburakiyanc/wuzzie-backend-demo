from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.EmailField(unique=True)
    gold = models.IntegerField(default=0)
    diamond = models.IntegerField(default=0)

    def _str_(self):
        return f"{self.username} and {self.email}"

User._meta.get_field('groups').remote_field.related_name = 'user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'
class Companion(models.Model):
    companion_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.user_id.username} and {self.name}"


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_value = models.IntegerField(default=0)

    # the item types are top, bottom, outerwear, footwear, jewelry, eyewear
    TOP = "top"
    BOTTOM = "bottom"
    OUTERWEAR = "outerwear"
    FOOTWEAR = "footwear"
    JEWELRY = "jewelry"
    EYEWEAR = "eyewear"

    ITEM_TYPES = {
        (TOP, "Top"),
        (BOTTOM, "Bottom"),
        (OUTERWEAR, "Outerwear"),
        (FOOTWEAR, "Footwear"),
        (JEWELRY, "Jewelry"),
        (EYEWEAR, "Eyewear")
    }
    item_types = models.CharField(
        max_length=10,
        choices=ITEM_TYPES,
    )

    def _str_(self):
        return f"{self.item_name} and {self.item_value}"


class CompanionItems(models.Model):
    companion_item_id = models.IntegerField(primary_key=True)
    companion_id = models.ForeignKey(Companion, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def _str_(self):
        return f"{self.companion_id.name} {self.item_id.item_name}and {self.quantity}"


class CompanionNeeds(models.Model):
    companion_need_id = models.IntegerField(primary_key=True)
    companion_id = models.ForeignKey(Companion, on_delete=models.CASCADE)
    starvation = models.IntegerField(default=100)  #0 means starving, 100 means full
    thirst = models.IntegerField(default=100)  #0 means dehydrated, 100 means hydrated
    energy = models.IntegerField(default=100)  #0 means asleep, 100 means awake
    nature_call = models.IntegerField(default=0)  #0 means no, 1 means yes
    last_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.companion_id.name} and {self.starvation} and {self.thirst} and {self.energy} and {self.nature_call}"
