import { Link } from 'react-router-dom';
import { useState } from 'react';

import cleffyTitle from './assets/cleffy_neutral.png'
import backgroundImage from './assets/upgraded_background_title.png'
import infoIcon from './assets/info.png'
import settingsIcon from './assets/settings.png'
import userIcon from './assets/user.png'



export default function TitlePage() {

    return (
        <>
        <div 
            className="page-background"
            style={{
                backgroundImage:`url(${backgroundImage})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
                backgroundRepeat: 'no-repeat',
                width: '100vw',
                height: '100vh',
                position: 'fixed', 
                top: '0',
                bottom: '0',
                left: '0',
                overflow: 'hidden',
                maxHeight: '100vh'
            }}
        >
            <div className="title">
                <img src={cleffyTitle} className="logo-cleffy" alt="Cleffy logo" />
            </div>
            <div className="buttons-container">
                <div className="gamemode-buttons-container"> {/* this contains the buttons of casual, competitive, and practice */}
                    <Link>
                        <button className="gamemode" id="casual">
                            casual
                        </button>
                    </Link>
                    <Link to="/competitive">
                        <button className="gamemode" id="competitive">
                            competitive
                        </button>
                    </Link>
                    <Link to="/practice">
                        <button className="gamemode" id="practice">
                            practice
                        </button>
                    </Link>
                </div>
                <div className="options-buttons-container"> {/* this contains the buttons of options, settings, and profile */}
                    <button className="options">
                       <img src={infoIcon} className="info-icon" alt="Info icon" />
                    </button>
                    <button className="options">
                        <img src={settingsIcon} className="settings-icon" alt="Settings icon" />
                    </button>
                    <button className="options">
                        <img src={userIcon} className="user-icon" alt="User icon" />
                    </button>
                </div>
            </div>
                
        </div>
            
        </>
    )
}