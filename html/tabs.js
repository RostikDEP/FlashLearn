async function sendWordToRecord() {
	let word = document.getElementById("inner_word").value;
	let translate = document.getElementById("inner_translate").value;
	let sentence = document.getElementById("inner_sentence").value;
	// FormBlink("red");

	await eel.AddWord(word, translate, sentence);
};
	
let sendButton = document.getElementById("add_button");
sendButton.onclick = sendWordToRecord;


function FormBlink(color) {
	document.getElementById("add_form_block").classList.add(color);
	setTimeout(function() {document.getElementById("add_form_block").classList.remove(color);}, 1000);
};


function ClearInputs(){
	document.getElementById("inner_word").value = "";
	document.getElementById("inner_translate").value = "";
	document.getElementById("inner_sentence").value = "";
}


eel.expose(FormBlink);
eel.expose(ClearInputs)