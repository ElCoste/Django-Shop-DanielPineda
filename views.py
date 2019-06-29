# aqui comienza la definicion checking
def checking(request):
    #A el formulario (CheckForm) se le trae el objeto instanciado y se le invoca y envia
    #el metodo from_class
    Checkform = self.from_class(request.POST)
    #aqui comienza un if para confirmar que el formulario Checkform es valido
    if Checkform.is_valid():
        #sí si es valido se guarda el formulario
        solicitud = Checkform
        solicitud.save()
        #aqui se retorna a la redireccion y se vuelve a traer el objeto instanciado y 
        #esta vez se le invoca el metodo get_success_url
        return HttResponseRedirect(self.get_success_url())
    else:
        #sí no es valido se retorna el objeto instanciado al que se le invoca el metodo
        #render_to_response y tambien se trae otra vez el objeto instanciado y se le
        #invoca el metodo get_context_data
        return self.render_to_response(self.get_context_data(form=form))
    #luego de todo el proceso de if se retorna a la vista checkout
    return render(request, 'dailyShop/checkout.html')

def factura(request):
    return render(request, 'dailyShop/factura.html')    