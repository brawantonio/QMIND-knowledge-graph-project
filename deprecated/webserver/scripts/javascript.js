function clk()  {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/test?text=" + document.getElementById("searchbar").value, true);
    xhr.responseType = "text";
    xhr.onload = function(e) {
        graph(JSON.parse(xhr.response));
        document.getElementById("blurbtext").innerHTML = "Success!"
    }
    xhr.onerror = function(e) {
        console.log(xhr.response);
        document.getElementById("blurbtext").innerHTML = "AJAX Failed"
    }
    xhr.send();
}

function graph(jsonobj) {
  
  // Formatting the data into graphable arrays
  var words = []
  var coords = []
  for (var x in jsonobj){
    words.push(x)
    coords.push(jsonobj[x])
  }

  const radius = 4

  // Getting context and setting the graph 
  const data =  {
      datasets: [{
        label: "Query Response",
        labels: words,
        data: coords
      }]
  };

  const config =  {
    type:'scatter',
    data: data,
    options: {
      response: true,
      title: {
        display: false,
        text: 'Original Data'
      },
      showLines: false,
      elements: {
        point: {
          pointStyle: 'circle',
          borderColor: "rgb(65,160,123)",
          backgroundColor: "rgb(36,124,142)",
          radius: radius
        }
      },
    },
    
    plugins: {
        afterDatasetsDraw: function(chart, args, options) {
            const ctx = chart.chart.ctx;
            ctx.save();
            // console.log(chart)
            ctx.font = '12px sans-serif';

            const ds = chart.data.datasets[0];
            const len = ds.data.length
            console.log(len)

            for(var i = 0; i < len; i++){
              var meta_mod = chart.getDatasetMeta(0).data[i]._model
              const textWidth = ctx.measureText(ds.labels[i]).width
              ctx.fillText(ds.labels[i], meta_mod.x - textWidth/2, meta_mod.y - 2 * radius - (11));
              
            }
        }
      }

  };
  
  const myChart = new Chart(
    document.getElementById('chart1').getContext("2d"), 
    config
  );


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
          
          voice.stop();

          // voice.sform.submit();
          // OR RUN AN AJAX/FETCH SEARCH
          document.getElementById("searchbar").value = said;

          clk();
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
      document.getElementById("mic_container").className="active";
      console.log('on')
    },
   
    // (C) STOP/CANCEL SPEECH RECOGNITION
    stop : () => {
      voice.recog.stop();
      voice.sbtn.onclick = voice.start;
      document.getElementById("mic_container").className="";
      console.log('off')
    }
  };
  window.addEventListener("DOMContentLoaded", voice.init);