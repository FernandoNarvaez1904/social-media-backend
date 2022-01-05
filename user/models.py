from django.contrib.auth.models import AbstractUser
from django.db import models


def _get_default_user_metadata():
    return {
        "approved_friend_request": []
    }


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    friends = models.ManyToManyField('self')
    meta_data = models.JSONField(default=_get_default_user_metadata)

    def _get_valid_pending_friend_request(self, request_id) -> "FriendRequest":
        request = self.receiver_friend_requests.filter(pk=request_id)

        if not request:
            raise Exception(f"User has not Friend Request {request_id}")
        elif request[0].status != FriendRequest.RequestStatus.PENDING:
            raise Exception("Friend Request is not pending")
        elif self.id != request[0].receiver.id:
            raise Exception("Only Receivers can mutate friend requests")

        return request[0]

    def accept_friend_request(self, request_id) -> None:
        request = self._get_valid_pending_friend_request(request_id)
        self.meta_data["approved_friend_request"].append(f"{request_id}")
        self.save()
        request.accept()

    def reject_friend_request(self, request_id) -> None:
        request = self._get_valid_pending_friend_request(request_id)
        request.reject()

    def send_friend_request(self, user_id) -> bool:
        user = self.__class__.objects.filter(pk=user_id)
        if not user:
            raise Exception("User does not exist")
        if user[0].id == self.id:
            raise Exception("Cannot sent friend request to itself")
        f_req = FriendRequest.objects.create(sender=self, receiver=user[0])
        f_req.save()
        return True

    def delete_friend_request(self, request_id) -> bool:
        request = self._get_valid_pending_friend_request(request_id)
        request.delete()
        return True


class FriendRequest(models.Model):
    class RequestStatus(models.TextChoices):
        ACCEPTED = 'A', "Accepted"
        REJECTED = 'R', "Rejected"
        PENDING = 'P', "Pending"

    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=RequestStatus.choices, default=RequestStatus.PENDING)
    sender = models.ForeignKey(User, related_name="sent_friend_requests", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver_friend_requests", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Prevents for re-adding the same user as friend
        already_friends = self.sender.friends.filter(pk=self.receiver.id).exists()
        if already_friends:
            raise Exception(f"{self.receiver} is already friends with {self.sender}")

        super(FriendRequest, self).save(*args, **kwargs)

    def accept(self) -> None:
        if self.status != self.RequestStatus.PENDING:
            raise Exception("Only pending requests can be accepted")

        receiver_user = self.receiver

        # Request has to been approved to change in the user model
        list_of_approved_request = receiver_user.meta_data["approved_friend_request"]
        if str(self.id) not in list_of_approved_request:
            raise Exception("Friends request can only be accepted in the User")

        # Adding sender to reciever friend list
        receiver_user.friends.add(self.sender)
        receiver_user.meta_data["approved_friend_request"].remove(str(self.id))
        receiver_user.save()

        # Updating Status
        self.status = self.RequestStatus.ACCEPTED
        self.save()  # Adding sender to reciever friend list

    def reject(self) -> None:
        receiver_user = self.receiver

        # Request has to been approved to change in the user model
        list_of_approved_request = receiver_user.meta_data["approved_friend_request"]
        if str(self.id) not in list_of_approved_request:
            raise Exception("Friends request can only be rejected in the User")

        self.status = self.RequestStatus.REJECTED
        self.save()
