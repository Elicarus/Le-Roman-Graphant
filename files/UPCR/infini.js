document.addEventListener( 'scroll', function () {
  var d = document.getElementById( 'endless' );
  texte = "\nd'un homme amoureux, \npicorant au hasard \ncomme un poulet sans tête, \nramassant les miettes\n"
  d.innerText = d.innerText + texte + texte + texte
});
