const card = document.querySelector(".card__inner");

card.addEventListener("click", function (e) {
  card.classList.toggle('is-flipped');
  if (!card.classList.contains('is-flipped')) {
    setTimeout(function() {
      configure_word();}, 300);}
});