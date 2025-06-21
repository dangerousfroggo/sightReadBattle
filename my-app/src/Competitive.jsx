import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import backgroundImage from './assets/background.png'

export default function Competitive() {
    const navigate = useNavigate();

    const [isCasual, setIsCasual] = useState(false)
    const [player1Finished, setPlayer1Finished] = useState(false);
    const [player2Finished, setPlayer2Finished] = useState(true); // to determine when we move onto the next screen?

    

    useEffect(() => {
        const goToResults = async () => {
            try {
                if (player1Finished && player2Finished) {
                    // Navigate to results page when both players have finished
                    navigate('/results');
                }
            } catch (error) {
                console.error("Error fetching results page:", error);
            }
        };
        goToResults();
    }, [player1Finished, player2Finished]);

    return (
        <>
            <div className="battlefield-container">
                <div 
                    className="battlefield"
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
                        maxHeight: '100vh',
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                    }}
                >
                    <div className="player-1-character">
                        {/* this is where player 1's character will be displayed */}
                    </div>

                    <div className="sheet-music-container">
                        {/* this is where the sheet music will be displayed*/}
                    </div>

                    <div className="player-2-character">
                        {/* this is where player 2's character will be displayed */}
                    </div>
                </div>
            </div>
        </>
    )
}


