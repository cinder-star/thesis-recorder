from handle_sentence.models import Recording


def get_recording_list(id=None):
    if id:
        queryset = Recording.objects.filter(user_id=id).values_list(
            "filename", flat=True
        )
    else:
        queryset = Recording.objects.all().values_list("filename", flat=True)
    return list(queryset)
