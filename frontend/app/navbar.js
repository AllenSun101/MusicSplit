"use client"

import { useState } from 'react'
import { Dialog, DialogPanel } from '@headlessui/react'
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline'
import Link from 'next/link';
import Image from 'next/image';

const navigation = [
    { name: 'Download Video', href: '/YouTubeDownload' },
	{ name: 'Split Music', href: '/SplitMusic' },
    { name: 'Join Music', href: '/JoinMusic' },
	{ name: 'Generate MIDI', href: '/GenerateMIDI' },
]

export default function Navbar(){
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

	return (
		<div className="bg-black">
			<header className="absolute inset-x-0 top-0 z-50">
				<nav className="flex items-center justify-between p-6 lg:px-6" aria-label="Global">
                    <div className="flex lg:flex-1">
						<Link href="/" className="-m-1.5 p-1.5 text-2xl font-semibold font-serif italic bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-purple-400">
                            MusicSplit
						</Link>
					</div>
					<div className="flex lg:hidden">
						<button
							type="button"
							className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-black"
							onClick={() => setMobileMenuOpen(true)}
						>
							<span className="sr-only">Open main menu</span>
							<Bars3Icon className="h-6 w-6" aria-hidden="true" />
						</button>
					</div>
					<div className="hidden lg:flex lg:gap-x-12 mx-12 my-4">
						{navigation.map((item) => (
							<Link key={item.name} href={item.href} className="text-md font-semibold leading-6 text-black">
								{item.name}
							</Link>
						))}
					</div>
				</nav>
                <Dialog as="div" className="lg:hidden" open={mobileMenuOpen} onClose={setMobileMenuOpen}>
                    <div className="fixed inset-0 z-50" />
                    <DialogPanel className="fixed inset-0 z-50 w-full h-full bg-gray-100 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
                    <div className="flex items-center justify-between">
                            <Link href="/" className="-m-1.5 p-1.5">
                                <span className="sr-only">MusicSplit</span>
                            </Link>
                            <button
                                type="button"
                                className="-m-2.5 rounded-md p-2.5 text-black"
                                onClick={() => setMobileMenuOpen(false)}
                            >
                                <span className="sr-only">Close menu</span>
                                <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                            </button>
                        </div>
                        <div className="mt-6 flow-root">
                            <div className="-my-6 divide-y divide-gray-500/10">
                                <div className="space-y-2 py-6">
                                    {navigation.map((item) => (
                                        <Link
                                        key={item.name}
                                        href={item.href}
                                        className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-black hover:bg-gray-200"
                                        onClick={() => setMobileMenuOpen(false)}
                                        >
                                        {item.name}
                                        </Link>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </DialogPanel>
                </Dialog>
			</header>
        </div>
    )}
