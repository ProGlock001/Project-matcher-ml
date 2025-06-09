import React, { useState } from 'react';
import axios from 'axios';

function UploadAndAnalyzeForm() {
  const [video, setVideo] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setVideo(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!video) return;

    const formData = new FormData();
    formData.append('file', video);

    try {
      const response = await axios.post('http://localhost:5000/analyze/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error uploading video:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileChange} />
      <button type="submit">Загрузить и проанализировать</button>
      {result && (
        <div>
          <h3>Тип личности: {result.mbti_type}</h3>
          <p>Рекомендуемая профессия: {result.profession}</p>
        </div>
      )}
    </form>
  );
}

export default UploadAndAnalyzeForm;
