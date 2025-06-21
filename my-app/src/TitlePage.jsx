import { Link } from 'react-router-dom';

import cleffyTitle from './assets/cleffy_neutral.png'
import backgroundImage from './assets/background.png'

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
                        <button className="gamemode">
                            casual
                        </button>
                    <Link to="/competitive">
                        <button className="gamemode">
                            competitive
                        </button>
                    </Link>
                        <button className="gamemode">
                            practice
                        </button>
                </div>
                <div className="options-buttons-container"> {/* this contains the buttons of options, settings, and profile */}
                    <button className="options">
                        Options
                    </button>
                    <button className="options">
                        Settings
                    </button>
                    <button className="options">
                        Profile
                    </button>
                </div>
            </div>
                
        </div>
            
        </>
    )
}