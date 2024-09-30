'use client'

import axios from 'axios';
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';

export default function JoinMusic() {
    const [files, setFiles] = useState([]);
    const [output, setOutput] = useState();

    const handleFileChange = (event) => {
        const selectedFiles = Array.from(event.target.files);
        setFiles(selectedFiles);
    };

    const submitFiles = () => {
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

            return axios.post(`http://localhost:8000/routes/join_stems/`, params, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': token,
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
        <div className='bg-white pt-24 pb-48 px-8'>
            <div className="flex justify-center mb-12 mt-12">
                <h2 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-500">
                Join Stems
                </h2>
            </div>
            <p className="text-lg text-center mb-24"> Join multiple .mp3 audio files. </p>
            <div className='mb-12 text-center'>
                <input
                    onChange={handleFileChange}
                    className='mb-6'
                    type="file"
                    multiple
                />
                {files.length > 0 && (
                    <div>
                        <h2 className='font-bold'>Selected Files:</h2>
                        <ul>
                            {files.map((file, index) => (
                                <li key={index}>{file.name}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
            <button className='mt-2 bg-gray-100 py-2 px-4 rounded-md block mx-auto' onClick={submitFiles}>
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
