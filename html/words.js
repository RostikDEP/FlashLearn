function setup_cardJS(word, translate, sentences){
	let frontWordH2 = document.getElementById('word_front');
	let frontTranslationH2 = document.getElementById('word_translate');
	let frontSentencesH2 = document.getElementById('word_sentences');

	frontWordH2.innerHTML = word;
	frontTranslationH2.innerHTML = translate;
	frontSentencesH2.innerHTML = sentences;
};
eel.expose(setup_cardJS);

async function configure_word(){
	await eel.GetRandomWordPy();
};

configure_word();