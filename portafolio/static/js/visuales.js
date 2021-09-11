function body_animation(){
    let body = document.getElementById('body');
    body.classList.add('body-animation');
}
setTimeout(body_animation, 2000)


var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

