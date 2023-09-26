from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from factures.models import Facture,LigneFacture
from .models import Payment
from products.models import Product
from .forms import PaymentForm  # Créez un formulaire pour enregistrer les paiements

from django.shortcuts import render, get_object_or_404, redirect
#from .models import Payment
from .forms import PaymentForm
from products.models import Product
from factures.models import Facture

def add_payment(request, pk):
    facture = get_object_or_404(Facture, pk=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.facture = facture  # Utilisez "facture" au lieu de "Facture"
            price = Product.objects.filter(price=price)
            # Récupérez le prix du produit associé à la facture (vous devez spécifier quel produit vous voulez ici)
            # Supposons que vous avez un lien entre la facture et le produit via la ligne de facture
            # Pour simplifier, je suppose que vous prenez le premier produit de la facture
            ligne_facture = facture.lignefacture_set.first()
            if ligne_facture:
                product_price = ligne_facture.produit.price
                payment.amount = product_price  # Définissez le montant du paiement sur le prix du produit
                
            payment.save()
            return redirect('facture_detail', pk=pk)
    else:
        form = PaymentForm()

    return render(request, 'payment/add_payment.html', {'form': form})
