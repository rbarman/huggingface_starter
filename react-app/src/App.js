import React, { useState,useEffect } from "react";
import axios from 'axios';

function App() {

  const [file, setFile] = useState();
  const [image_label, setImage_label] = useState();

  // mainly for debugging
  useEffect(() => {
    console.log("label : " + image_label)
  },[image_label])

  // When user upload an image, display the image and call model to classify the image
  function on_file_upload(event) {

    var file = event.target.files[0];
    // render the image
    setFile(URL.createObjectURL(file));

    // call the api
    var reader = new FileReader();
    reader.readAsDataURL(file);
    // reader gets the base64url of the image which is required for api call
    reader.onload = function(event) {
      axios
        .post('https://hf.space/embed/rbarman/resnet50-example/+/api/predict/', {
          data: [reader.result]
        })
        .then((res) => {
          console.log(res)
          setImage_label(res['data']['data'][0]['label'])  
        })
        .catch((err) => {
          console.log(err.message);
      });
    };
  }

  return (
    <div className="App">
      {image_label &&
        <div>
          <h2>Image is a <b>{image_label}</b></h2>
        </div>
      }
      {!image_label &&
        <h2>Upload an image</h2>
      }
      <input type="file" onChange={on_file_upload} />
      <img src={file} />
    </div>
  );
}

export default App;
