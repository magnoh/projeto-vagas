
window.addEventListener('load', () => {
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }


   const form = document.querySelector('#form-vaga')
   const cargoVaga = document.querySelector('#id_cargo_vaga')
   const descricaoVaga = document.querySelector('#id_descricao_vaga')
   const faixaSalarial = document.querySelector('#id_faixa_salarial')
   const escolaridade = document.querySelector('#id_escolaridade_vaga')

   const clearFormSubmit = () => {
    cargoVaga.value = ''
    descricaoVaga.value = ''
    faixaSalarial.value = ''
    escolaridade.value = ''
   }

   form.onsubmit = (e) => {
    // Evita comportamento de recarregamento padrão do formulario
    e.preventDefault()

    toastr.info('Vaga cadastrada com sucesso')

    // Invoca função p/ limpar campos
    clearFormSubmit()
   }
})
