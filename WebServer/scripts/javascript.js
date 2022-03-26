function clk()  {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/test?text=" + document.getElementById("searchbar").value, true);
    xhr.responseType = "text";
    xhr.onload = function(e) {
        document.getElementById("blurbtext").innerHTML = xhr.response
    }
    xhr.send();
}

document.getElementById("searchbar").addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        console.log("enter hit")
        clk();
    }
});

document.getElementById("micicon").onclick = function() {
    console.log("listening...")
};


var voice = {
    init : function () {
      // (A1) GET HTML ELEMENTS
      voice.sfield = document.getElementById("searchbar");
      voice.sbtn = document.getElementById("micicon");
   
      // (A2) GET MICROPHONE ACCESS
      navigator.mediaDevices.getUserMedia({ audio: true })
      .then((stream) => {
        // (A3) SPEECH RECOGNITION OBJECT + SETTINGS
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        voice.recog = new SpeechRecognition();
        voice.recog.lang = "en-US";
        voice.recog.continuous = false;
        voice.recog.interimResults = false;
   
        console.log('booted')
        // (A4) POPUPLATE SEARCH FIELD ON SPEECH RECOGNITION
        voice.recog.onresult = (evt) => {
          said = evt.results[0][0].transcript.toLowerCase();
          console.log(said);
          // voice.sform.submit();
          // OR RUN AN AJAX/FETCH SEARCH
          voice.stop();
        };
   
        // (A5) ON SPEECH RECOGNITION ERROR
        //voice.recog.onerror = (err) => { console.error(err); };
   
        // (A6) READY!
        voice.sbtn.disabled = false;
        voice.stop();
      })
    //   .catch((err) => {
    //     console.error(err);
    //     console.log("Please enable access and attach microphone.")
    //   });
    },
   
    // (B) START SPEECH RECOGNITION
    start : () => {
      voice.recog.start();
      voice.sbtn.onclick = voice.stop;
      console.log('on')
    },
   
    // (C) STOP/CANCEL SPEECH RECOGNITION
    stop : () => {
      voice.recog.stop();
      voice.sbtn.onclick = voice.start;
      console.log('off')
    }
  };
  window.addEventListener("DOMContentLoaded", voice.init);