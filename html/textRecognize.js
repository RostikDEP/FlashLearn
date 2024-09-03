let loadConfigButton = document.getElementById('config_load_button');
let recognizeButton = document.getElementById('recognize_button');

function loadConfigButton__click(){
	let x1 = document.getElementById("x1");
	let y1 = document.getElementById("y1");
	let x2 = document.getElementById("x2");
	let y2 = document.getElementById("y2");

	loadConfig();
}
async function loadConfig() {
    let cords = await eel.GetScreenConfig()();

    let x1 = document.getElementById("x1");
    let y1 = document.getElementById("y1");
    let x2 = document.getElementById("x2");
    let y2 = document.getElementById("y2");

    x1.value = cords[0];
    y1.value = cords[1];
    x2.value = cords[2];
    y2.value = cords[3];
}

async function recognizeButton__click(){
    await eel.AreaRecognize();
};

recognize_button.onclick = recognizeButton__click;
loadConfigButton.onclick = loadConfigButton__click;