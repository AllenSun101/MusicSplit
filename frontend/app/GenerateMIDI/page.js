'use client'

import axios from 'axios';
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';

export default function GenerateMIDI(){
	const [files, setFiles] = useState([]);
    const [output, setOutput] = useState();

    const handleFileChange = (event) => {
		const files = Array.from(event.target.files);
		setFiles(files);
	};

    const submitLink = () => {
        // Send file and fetch results
        mutation.mutate({ files: files }, {
            onSuccess: (data) => {
                setOutput(data.data.output);
            }
        });
        setFiles([]);
        setOutput();
    };

    // Send request to backend and fetch data
    const mutation = useMutation({
        mutationFn: async (params) => {
			const token = await fetchCSRFToken(); // Fetch the CSRF token

            axios.defaults.withCredentials = true; // Ensure credentials (cookies) are included

            return axios.post(`http://localhost:8000/routes/mp3_to_midi/`, 
                params
            , {
                headers: {
                    'X-CSRFToken': token,
                    'Content-Type': 'multipart/form-data',
                },
            });
        },
    });

    const fetchCSRFToken = async () => {
        try {
            const response = await axios.get('http://localhost:8000/routes/csrf-token/', { withCredentials: true });
            return response.data.csrfToken;
        } catch (error) {
            console.error('Error fetching CSRF token:', error);
        }
    };

    return (
        <div className='bg-white py-24 px-8'>
            <div className="flex justify-center mb-12">
                <h2 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-500">
                Generate MIDI
                </h2>
            </div>
            <p className="text-lg text-center mb-24">Get an .midi file from an .mp3 audio file.</p>
            <label className='text-lg mr-4'>Select File:</label>
            <input
                onChange={handleFileChange}
                className='mb-6'
                type="file"
            />
            {files.length > 0 && (
                <div>
                    <h2 className='font-bold'>Selected File:</h2>
                    <ul>
                        {files.map((file, index) => (
                            <li key={index}>{file.name}</li>
                        ))}
                    </ul>
                </div>
            )}
            <button className='mt-2 bg-gray-100 py-2 px-4 rounded-md block mx-auto' onClick={submitLink}>
                Submit
            </button>
            
            {output && (
                <div className="mt-4 text-center">
                    <p className='mb-4'>Your file is ready for download!</p>
                    <a 
                        href={output} 
                        download 
                        className='bg-purple-500 text-white py-2 px-4 rounded-md'>
                        Download MIDI
                    </a>
                </div>
            )}

        </div>
    );
}