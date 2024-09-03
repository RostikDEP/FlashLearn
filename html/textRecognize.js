let loadConfigButton = document.getElementById('config_load_button');
let recognizeButton = document.getElementById('recognize_button');

let textArea = document.getElementById('text_area');
let translateArea = document.getElementById('translate_area');

let x1 = document.getElementById("x1");
let y1 = document.getElementById("y1");
let x2 = document.getElementById("x2");
let y2 = document.getElementById("y2");



function loadConfigButton__click(){
	loadConfig();
}



async function loadConfig() {
    let cords = await eel.GetScreenConfig()();

    x1.value = cords[0];
    y1.value = cords[1];
    x2.value = cords[2];
    y2.value = cords[3];
}



async function recognizeButton__click(){
    await eel.AreaRecognize(x1.value, y1.value, x2.value, y2.value);
};



function FillTextData(text, translation){
    textArea.value = text;
    translateArea.value = translation;
};


eel.expose(FillTextData);
recognize_button.onclick = recognizeButton__click;
loadConfigButton.onclick = loadConfigButton__click;