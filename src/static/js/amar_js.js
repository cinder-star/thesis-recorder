let sentence_number = "";
let div = document.getElementById("record_box");
let text = document.getElementById("text");
let csrftoken = $("#record_box").find('input[name=csrfmiddlewaretoken]').val()

function get_sentence() {
	let fd = new FormData();
	let x = localStorage.getItem("text_list");
	$.ajaxSetup({
		data: {csrfmiddlewaretoken: csrftoken },
	});
	if (x==null || x.length >= 13) {
		x = "";
		localStorage.setItem("text_list", "");
	}
	fd.append("all_strings", x);
	$.ajax({
        headers: {
			"X-CSRFToken": csrftoken,
		},
        url: '/get_new_sentence/',
        type: 'POST',
        data: fd,
        async: true,
        contentType: false,
        processData: false,
    }).done((e) => {
		if(x==""){
			localStorage.setItem("text_list", e.number);
		} else {
			localStorage.setItem("text_list", x + ", "+e.number.toString());
		}
		text.innerHTML = e.sentence;
		sentence_number = e.number.toString();
    });
}

get_sentence();

/*
 * Date Format 1.2.3
 * (c) 2007-2009 Steven Levithan <stevenlevithan.com>
 * MIT license
 *
 * Includes enhancements by Scott Trenda <scott.trenda.net>
 * and Kris Kowal <cixar.com/~kris.kowal/>
 *
 * Accepts a date, a mask, or a date and a mask.
 * Returns a formatted version of the given date.
 * The date defaults to the current date/time.
 * The mask defaults to dateFormat.masks.default.
 */

var dateFormat = function () {
	var	token = /d{1,4}|m{1,4}|yy(?:yy)?|([HhMsTt])\1?|[LloSZ]|"[^"]*"|'[^']*'/g,
		timezone = /\b(?:[PMCEA][SDP]T|(?:Pacific|Mountain|Central|Eastern|Atlantic) (?:Standard|Daylight|Prevailing) Time|(?:GMT|UTC)(?:[-+]\d{4})?)\b/g,
		timezoneClip = /[^-+\dA-Z]/g,
		pad = function (val, len) {
			val = String(val);
			len = len || 2;
			while (val.length < len) val = "0" + val;
			return val;
		};

	// Regexes and supporting functions are cached through closure
	return function (date, mask, utc) {
		var dF = dateFormat;

		// You can't provide utc if you skip other args (use the "UTC:" mask prefix)
		if (arguments.length == 1 && Object.prototype.toString.call(date) == "[object String]" && !/\d/.test(date)) {
			mask = date;
			date = undefined;
		}

		// Passing date through Date applies Date.parse, if necessary
		date = date ? new Date(date) : new Date;
		if (isNaN(date)) throw SyntaxError("invalid date");

		mask = String(dF.masks[mask] || mask || dF.masks["default"]);

		// Allow setting the utc argument via the mask
		if (mask.slice(0, 4) == "UTC:") {
			mask = mask.slice(4);
			utc = true;
		}

		var	_ = utc ? "getUTC" : "get",
			d = date[_ + "Date"](),
			D = date[_ + "Day"](),
			m = date[_ + "Month"](),
			y = date[_ + "FullYear"](),
			H = date[_ + "Hours"](),
			M = date[_ + "Minutes"](),
			s = date[_ + "Seconds"](),
			L = date[_ + "Milliseconds"](),
			o = utc ? 0 : date.getTimezoneOffset(),
			flags = {
				d:    d,
				dd:   pad(d),
				ddd:  dF.i18n.dayNames[D],
				dddd: dF.i18n.dayNames[D + 7],
				m:    m + 1,
				mm:   pad(m + 1),
				mmm:  dF.i18n.monthNames[m],
				mmmm: dF.i18n.monthNames[m + 12],
				yy:   String(y).slice(2),
				yyyy: y,
				h:    H % 12 || 12,
				hh:   pad(H % 12 || 12),
				H:    H,
				HH:   pad(H),
				M:    M,
				MM:   pad(M),
				s:    s,
				ss:   pad(s),
				l:    pad(L, 3),
				L:    pad(L > 99 ? Math.round(L / 10) : L),
				t:    H < 12 ? "a"  : "p",
				tt:   H < 12 ? "am" : "pm",
				T:    H < 12 ? "A"  : "P",
				TT:   H < 12 ? "AM" : "PM",
				Z:    utc ? "UTC" : (String(date).match(timezone) || [""]).pop().replace(timezoneClip, ""),
				o:    (o > 0 ? "-" : "+") + pad(Math.floor(Math.abs(o) / 60) * 100 + Math.abs(o) % 60, 4),
				S:    ["th", "st", "nd", "rd"][d % 10 > 3 ? 0 : (d % 100 - d % 10 != 10) * d % 10]
			};

		return mask.replace(token, function ($0) {
			return $0 in flags ? flags[$0] : $0.slice(1, $0.length - 1);
		});
	};
}();

// Some common format strings
dateFormat.masks = {
	"default":      "ddd mmm dd yyyy HH:MM:ss",
	shortDate:      "m/d/yy",
	mediumDate:     "mmm d, yyyy",
	longDate:       "mmmm d, yyyy",
	fullDate:       "dddd, mmmm d, yyyy",
	shortTime:      "h:MM TT",
	mediumTime:     "h:MM:ss TT",
	longTime:       "h:MM:ss TT Z",
	isoDate:        "yyyy-mm-dd",
	isoTime:        "HH:MM:ss",
	isoDateTime:    "yyyy-mm-dd'T'HH:MM:ss",
	isoUtcDateTime: "UTC:yyyy-mm-dd'T'HH:MM:ss'Z'"
};

// Internationalization strings
dateFormat.i18n = {
	dayNames: [
		"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
		"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
	],
	monthNames: [
		"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
		"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	]
};

// For convenience...
Date.prototype.format = function (mask, utc) {
	return dateFormat(this, mask, utc);
};

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
            sendData(blob)
        }
    }
}

function sendData(data) {
    let fd = new FormData();
    let now = new Date();
	let nowstring = now.format("yyyymmddHHMMss");
	let x = localStorage.getItem("text_list");
	if (x==null || x.length >= 13) {
		x = "";
		localStorage.setItem("text_list", "");
	}
    fd.append("audio", data);
	fd.append("filename", sentence_number+"-"+nowstring+".wav");
	fd.append("all_strings", x);
    $.ajax({
        headers: {
			"X-CSRFToken": csrftoken,
		},
        url: '/send/',
        type: 'POST',
        data: fd,
        async: true,
        contentType: false,
        processData: false,
    }).done((e) => {
		if(x==""){
			localStorage.setItem("text_list", e.number);
		} else {
			localStorage.setItem("text_list", x + ", "+e.number.toString());
		}
		text.innerHTML = e.sentence;
		sentence_number = e.number.toString();
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