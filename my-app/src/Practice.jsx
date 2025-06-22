import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import backgroundImage from './assets/upgraded_background_title.png'
import player1Sprite from './assets/player-1-sprite.png'
import sheetMusic from './assets/sheet-music.png'


export default function Practice() {
    const [playerAccuracy, setPlayerAccuracy] = useState("50%") // Example heights, adjust as needed
    const navigate = useNavigate();

    const [player1Finished, setPlayer1Finished] = useState(false);

    useEffect(() => {
        const goToResults = async () => {
            try {
                if (player1Finished) {
                    // Navigate to results page when both players have finished
                    navigate('/results');
                }
            } catch (error) {
                console.error("Error fetching results page:", error);
            }
        };
        goToResults();
    }, [player1Finished]);

    // useEffect(() => {
    //     const displayPlayerAccuracy = () => {
    //         try {

    //         } catch {
    //             console.error("Error displaying player accuracy:", error);
    //         }
    //     }
    // }, [])

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
                    <div className="player-1-stats">
                        <div className="player-1-bar">
                            <div 
                                className="player-1-accuracy"
                                style={{ height: playerAccuracy }}
                            />
                        </div>
                        <img src={player1Sprite} className="player-1-sprite" alt="Player 1 Sprite" />
                    </div>

                    <div className="sheet-music-container">
                        <img src={sheetMusic} className="sheet-music" alt="Sheet Music" /> 
                    </div>
                </div>
            </div>
        </>
    )
}
