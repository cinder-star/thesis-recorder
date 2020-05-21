let sentence_number = "";
let div = document.getElementById("record_box");
let text = document.getElementById("text");

function set_sentence() {
	let fd = new FormData();
	let x = sessionStorage.getItem("text_list");
	if (x==null || x.length >= 13) {
		x = "";
		localStorage.setItem("text_list", "");
	}
	fd.append("all_strings", x);
	$.ajax({
        url: '/get_new_sentence',
        type: 'POST',
        data: fd,
        async: true,
        contentType: false,
        processData: false,
    }).done((e) => {
		if(x==""){
			sessionStorage.setItem("text_list", e.number);
		} else {localStorage
			sessionStorage.setItem("text_list", x + ", "+e.number.toString());
		}
		text.innerHTML = e.sentence;
		sentence_number = e.number.toString();
    });
}

set_sentence();

Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}


navigator.mediaDevices.getUserMedia({
        audio: true
    })
    .then(stream => {
        handlerFunction(stream)
    })


function handlerFunction(stream) {
    let audioChunks = [];
    rec = new MediaRecorder(stream);
    rec.ondataavailable = (e) => {
		audioChunks = []
        audioChunks.push(e.data);
        if (rec.state == "inactive") {
            let blob = new Blob(audioChunks, {
                type: 'audio/wav; codecs=MS_PCM'
            });
            recordedAudio.src = URL.createObjectURL(blob);
            recordedAudio.controls = true;
            recordedAudio.autoplay = true;
            set_sentence();
            sendData(blob);
        }
    }
}

async function sendData(data) {
    let fd = new FormData();
    let now = new Date();
	let nowstring = now.format("yyyymmddHHMMss");
	let x = localStorage.getItem("text_list");
    fd.append("audio", data);
	fd.append("filename", sentence_number+"-"+nowstring+".wav");
    $.ajax({
        url: '/send',
        type: 'POST',
        data: fd,
        async: true,
        contentType: false,
        processData: false,
    }).done((e) => {
        console.log(e)
    });
}

record.onclick = (e) => {
	document.getElementById("recordedAudio").remove();
	let audio_recorder = document.createElement("audio");
	audio_recorder.setAttribute("id", "recordedAudio");
	div.appendChild(audio_recorder);

    record.disabled = true;
    stopRecord.disabled = false;
    audioChunks = [];
    rec.start();
}

stopRecord.onclick = (e) => {
    record.disabled = false;
    stop.disabled = true;
    rec.stop();
}