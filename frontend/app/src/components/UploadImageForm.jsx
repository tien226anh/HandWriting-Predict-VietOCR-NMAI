import React, { useState } from 'react';

const UploadImageForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [filename, setFileName] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await fetch('http://localhost:8000/upload-image/', {
          method: 'POST',
          body: formData,
        });

        const data = await response.json();
        setResult(data.result);
        setFileName(data.filename);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  return (
    <div className="container">
      <div className="row mt-4">
        <div
        // className="col-md-6 offset-md-3"
        >
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Upload Image</h5>
              <input type="file" className="form-control" onChange={handleFileChange} />
              <button className="btn btn-primary mt-3" onClick={handleUpload}>Upload</button>
            </div>
          </div>
        </div>
      </div>
      {result && (
        <div className="row mt-3">
          <h5>Result: {result}</h5>
          <div className='card'>
            <img src={`http://localhost:8000/static/${filename}`} alt="Uploaded" className="img-fluid mt-3 card-body" />
          </div>
        </div>
      )}
    </div>
  );
};

export default UploadImageForm;
