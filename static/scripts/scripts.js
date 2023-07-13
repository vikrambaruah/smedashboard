const xValues = [100,200,300,400,500,600,700,800,900,1000];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
      borderColor: "red",
      fill: false
    },{
      data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
      borderColor: "green",
      fill: false
    },{
      data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
      borderColor: "blue",
      fill: false
    }]
  },
  options: {
    legend: {display: false}
  }
});
// import fs from 'fs';
// import { XMLParser} from 'fast-xml-parser';
// import xml2js from 'xml2js';
// import xl from 'excel4node';
// function fetchData(){

//     fetch("http://mtconnect.mazakcorp.com:5609/sample")
//     .then(response=>response.text())
//     .then(data=>{
//         const wb = new xl.Workbook();
//         const ws = wb.addWorksheet('MTConnect');
//         //let parser=new XMLParser();
//         var parser = new xml2js.Parser({explicitArray: false});
//         //let xml=parser.parseString(data);
//         parser.parseString(data, function (err, result) {
//             if (err) {
//                 console.error('xml2js.parseString: Error occurred: ', err);
//             } else {
//                 // for (let key in Object.keys(result.MTConnectStreams.Streams.DeviceStream.ComponentStream)){
//                 //     console.log(result.MTConnectStreams.Streams.DeviceStream.ComponentStream[key]);
                    
//                 // }
//                 //console.log(JSON.stringify(result, null, 2));
//                 for (let k=0; k<Object.values(result.MTConnectStreams.Streams.DeviceStream.ComponentStream).length;k++){
//                 //console.log(Object.values(result.MTConnectStreams.Streams.DeviceStream.ComponentStream[k])[0]['name']);
//                 for (let i=1;i<Object.values(result.MTConnectStreams.Streams.DeviceStream.ComponentStream[k]).length;i++){
//                     for (let j in Object.values(result.MTConnectStreams.Streams.DeviceStream.ComponentStream[1])[i]){
//                         console.log(Object.values(result.MTConnectStreams.Streams.DeviceStream.ComponentStream[1])[j]['_']);

//                     }
//                 }
//                 }
                
//             }
//         });
//         // const content=[];
//         // // try {
//         // //     fs.writeFileSync('test.txt', JSON.stringify(xml.MTConnectStreams.Streams.DeviceStream.ComponentStream[0]));
//         // // } catch (err) {
//         // //     console.error(err);
//         // // }
//         // console.log(xml.MTConnectStreams.Streams.DeviceStream.ComponentStream[0].getAttribute('name'));
//         // for (let i=0;i<xml.MTConnectStreams.Streams.DeviceStream.ComponentStream.length;i++){
//         // //document.getElementById('output').innerHTML=data;
//         // //const fs = require('fs');

//         //     //console.log(xml.MTConnectStreams.Streams.DeviceStream.ComponentStream[i]);
//         //     content[i]=JSON.stringify(xml.MTConnectStreams.Streams.DeviceStream.ComponentStream[i]);
//         //     console.log(content[i]);
//         //     // fs.appendFile('test.txt', content[i], err => {
//         //     //     if (err) {
//         //     //       console.error(err);
//         //     //     }
//         //     //   });
            
//         //}
//     })  
// }

//    fetchData();
// // function readXML(){
// //     var xml=new XMLHttpRequest();
// //     xml.open('GET','mtconnect.xml',false);
// //     xml.send();
// //     var xmlData=xml.responseText;
// //     console.log(xmlData);
// // }
// // readXML();

