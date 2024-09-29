'use client'

import axios from 'axios';
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';

export default function YouTubeDownload() {
    const [link, setLink] = useState();
    const [output, setOutput] = useState();

    const handleLinkChange = (event) => {
        const selectedLink = event.target.value;
        setLink(selectedLink);
    };

    const submitLink = () => {
        // Send link and fetch results
        mutation.mutate({ link }, {
            onSuccess: (data) => {
                setOutput(data.data.output);
            }
        });
    };

    // Send request to backend and fetch data
    const mutation = useMutation({
        mutationFn: async (params) => {
			const token = await fetchCSRFToken(); // Fetch the CSRF token

            axios.defaults.withCredentials = true; // Ensure credentials (cookies) are included

            return axios.post(`http://localhost:8000/routes/yt_to_mp3/`, {
                link: params.link,
            }, {
                headers: {
                    'X-CSRFToken': token,
                    'Content-Type': 'application/json',
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
                YouTube Download
                </h2>
            </div>
            <p className="text-lg text-center mb-24">Get an .mp3 file from a YouTube link.</p>
            <label className='text-lg mr-4'>Enter text:</label>
            <input
                onChange={handleLinkChange}
                className='mb-6 rounded-md border border-blue-500'
                type="text"
                name="link"
            />
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
                        Download MP3
                    </a>
                </div>
            )}

        </div>
    );
}
