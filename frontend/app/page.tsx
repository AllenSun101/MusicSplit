import Image from "next/image";

export default function Home() {
  return (
    <div className="bg-white py-24">
      <div className="hero h-[70vh] bg-cover bg-center relative" style={{ backgroundImage: 'url("/Hero.jpg")' }}>
          	<div className="absolute inset-0 bg-white bg-opacity-30"></div>
            <div className="hero-content text-center absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                <div className="max-w-screen-md">
                    <span className="text-5xl font-bold">Welcome to </span>
                    <span className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-500">MusicSplit</span>
                    <p className="py-6 text-xl mb-6">
                        Build personalized resumes in seconds
                    </p>
                </div>
            </div>
        </div>
        <div className="lg:px-24 px-8 text-lg mt-12">
          <p>MusicSplit provides a suite of music processing tools, designed for ordinary hobbyists! It is designed 
            to provide free services for downloading, splitting, and converting music files.
          </p>
        </div>
        <div className="mt-12 text-center">
          <h2 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-500">
            Tools
          </h2>
        </div>
        <div>
        <section className="p-6 dark:bg-gray-100 dark:text-gray-800">
	        <div className="container mx-auto">
		        <div className="grid gap-6 mt-6 lg:grid-cols-3">
              <div className="flex flex-col p-8 space-y-4 dark:bg-gray-50 bg-gradient-to-br from-blue-100 to-purple-100 rounded-lg shadow-lg border-8 border-purple-200">
                <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full bg-purple-300 dark:text-gray-50">1</div>
                <p className="text-2xl font-semibold">
                  <b>Download</b> music files from YouTube directly in a safe and secure manner.
                </p>
              </div>
              <div className="flex flex-col p-8 space-y-4 dark:bg-gray-50 bg-gradient-to-br from-blue-100 to-purple-100 rounded-lg shadow-lg border-8 border-purple-200">
                <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full bg-purple-300 dark:text-gray-50">2</div>
                <p className="text-2xl font-semibold">
                  <b>Split</b> music files into individual stems for further processing. 
                </p>
              </div>
              <div className="flex flex-col p-8 space-y-4 dark:bg-gray-50 bg-gradient-to-br from-blue-100 to-purple-100 rounded-lg shadow-lg border-8 border-purple-200">
                <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full bg-purple-300 dark:text-gray-50">3</div>
                <p className="text-2xl font-semibold">
                  <b>Convert</b> music files into AI-based estimates of sheet music. 
                </p>
              </div>
            </div>
          </div>
        </section>
        </div>
    </div>
  );
}
