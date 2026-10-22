from .models import ProfilOrganisasi, TautanTerkait


def organisasi(request):
    return {
        "profil": ProfilOrganisasi.objects.first(),
        "tautan_terkait": TautanTerkait.objects.all(),
    }