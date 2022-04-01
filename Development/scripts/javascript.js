function clk()  {
    rev_load();
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/test?text=" + document.getElementById("searchbar").value, true);
    xhr.responseType = "text";
    xhr.onload = function(e) {
        console.log(JSON.parse(xhr.response))
        graph(JSON.parse(xhr.response));
        document.getElementById("blurbtext").innerHTML = "Success!"
        hide_load();
        document.getElementById("chart1").className="active";
    }
    xhr.onerror = function(e) {
        console.log(xhr.response);
        document.getElementById("blurbtext").innerHTML = "AJAX Failed"
        hide_load();
    }
    xhr.send();
}

function graph(jsonobjlist) {
  
  // Formatting the data into graphable arrays
  var urls      = []
  var labels    = []
  var coords    = []
  var cos       = []

  for (var i = 0 ; i < jsonobjlist.length; i++) {
      console.log(jsonobjlist[i])
      urls.push(jsonobjlist[i]["url"]);
      labels.push(jsonobjlist[i]["url"].split("/")[6]);

      // TRANSLATIONS
        // x = (1-cos_dist)cos(4*atan2(Pca_x,Pca_y))
        // y = (1-cos_dist)sin(4*atan2(Pca_x,Pca_y))
      let pca_x = jsonobjlist[i]["pca_x"]
      let pca_y = jsonobjlist[i]["pca_y"]
      let cos_dist = jsonobjlist[i]["cos_dist"]

      coords.push({
          x: (1-cos_dist) * Math.cos( 4 * Math.atan2(pca_x, pca_y) ),
          y: (1-cos_dist) * Math.sin( 4 * Math.atan2(pca_x, pca_y) )
      });
      cos.push(jsonobjlist[i]["cos_dist"]);
  }


  var pointRadius=[];

  // Getting context and setting the graph 
  const data =  {
      datasets: [{
        label: "Query Response",
        labels: labels,
        data: coords,
        pointStyle: 'circle',
        pointBackgroundColor: "rgb(36,124,142)",
        pointRadius: pointRadius
      }]
  };

  const config =  {

    type:'scatter',

    data: data,

    options: {

      hover: {
        mode: null,
      },

      response: true,

      title: {
        display: false,
        text: 'Original Data'
      },

      legend:{
        display:false
      },

      showLines: false,

      scales:{
        yAxes:[{
          beginAtZero:true,
          gridLines:{
            drawBorder:false,
            display:false
          },
          ticks:{
            display:false,
          }
          
        }],
        xAxes:[{
          beginAtZero:true,
          gridLines:{
            drawBorder:false,
            display:false
          },
          ticks:{
            display:false,
          }
        }]
      },


      onClick(e) {
       
        const activePoints = myChart.getElementsAtEventForMode(e, 'nearest', {
          intersect: true
        }, false)

        //console.log(urls[activePoints[0]._index])
        window.location.href = urls[activePoints[0]._index];

      }

    },
    
    plugins: {
        afterDatasetsDraw: function(chart, args, options) {
            const ctx = chart.chart.ctx;
            ctx.save();
            // console.log(chart)
            ctx.font = '12px sans-serif';

            const ds = chart.data.datasets[0];
            const len = ds.data.length

            for(var i = 0; i < len; i++){
              var meta_mod = chart.getDatasetMeta(0).data[i]._model
              const textWidth1 = ctx.measureText(ds.labels[i]).width
              ctx.fillText(ds.labels[i], meta_mod.x - textWidth1/2, meta_mod.y - (2*pointRadius[i]));
              
            }

            let qtext = document.getElementById("searchbar").value
            qtext = qtext.split(" ");

            for (let i = 0; i < qtext.length; i++) {
                qtext[i] = qtext[i][0].toUpperCase() + qtext[i].substr(1);
            }

            qtext = qtext.join(" ");
            

            const textWidth2 = ctx.measureText(qtext).width

            ctx.fillText(qtext, chart.chart.width/2 - textWidth2/2, chart.chart.height/2);

            
        
         }
      }

  };
  
  const myChart = new Chart(
    document.getElementById('chart1').getContext("2d"), 
    config
  );

  let baseRad = 6
  for(var i=0; i < cos.length ; i = i + 1){
    pointRadius.push((cos[i] + 1) * baseRad);
  }

  myChart.update()



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



function rev_load(){
  document.querySelector(".loading-overlay").hidden                  = false
  document.querySelector(".loading-overlay-image-container").hidden  = false
}

function hide_load(){
  document.querySelector(".loading-overlay").hidden                  = true
  document.querySelector(".loading-overlay-image-container").hidden  = true
}

window.addEventListener('DOMContentLoaded', (event) => {
    hide_load()
});