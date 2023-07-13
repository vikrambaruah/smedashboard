import fs from 'fs';
import { XMLParser} from 'fast-xml-parser';
import xml2js from 'xml2js';
import xl from 'xlsx';

function fetchData() {
    fetch('http://mtconnect.mazakcorp.com:5609/sample')
      .then((response) => response.text())
      .then((data) => {
        const wb = xl.utils.book_new();
        const ws = xl.utils.aoa_to_sheet([]);
        xl.utils.book_append_sheet(wb, ws, 'MTConnect');
  
        var parser = new xml2js.Parser({ explicitArray: false });
        parser.parseString(data, function (err, result) {
          if (err) {
            console.error('xml2js.parseString: Error occurred: ', err);
          } else {
            const componentStreams = result.MTConnectStreams.Streams.DeviceStream.ComponentStream;
  
            for (let k = 0; k < componentStreams.length; k++) {
              const componentName = Object.values(componentStreams[k])[0]['name'];
              const componentStream = componentStreams[k];
              const keys = Object.keys(componentStream);
              for (let i = 0; i < keys.length; i++) {
                const key = keys[i];
                if (key !== 'name') {
                  const subComponent = componentStream[key];
                  const subComponentKeys = Object.keys(subComponent);
                  for (let j = 0; j < subComponentKeys.length; j++) {
                    const subKey = subComponentKeys[j];
                    const valueObject = subComponent[subKey];
                    let values = [];

                  if (Array.isArray(valueObject)) {
                    values = valueObject.map((obj) => obj._).filter(Boolean);
                  } else if (valueObject && valueObject._) {
                    //values.push(valueObject._);
                  }
                    const rowIndex = k * subComponentKeys.length + i + 1;
                    console.log(values);
                    values.forEach((value, index) => {
                        const cellRef = xl.utils.encode_cell({ r: rowIndex + index, c: j });
                        xl.utils.sheet_add_aoa(ws, [[componentName, subKey, value]], { origin: cellRef });
                      });
                  }
                }
              }
            }
  
            xl.writeFile(wb, 'data.xlsx');
            console.log('Data written to data.xlsx');
          }
        });
      });
  }
  
  fetchData();
