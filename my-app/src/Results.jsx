import { useState, useEffect } from "react"
import { useLocation } from "react-router-dom"

import resultsBackground from './assets/results_background.png'
import player2Sprite from './assets/player-2-sprite.png'
import player1Sprite from './assets/player-1-sprite.png'

export default function Results() {
    const location = useLocation();
    const [endingMessage, setEndingMessage] = useState("")
    const [player1Height, setPlayer1Height] = useState("50%") // Example heights, adjust as needed
    const [player2Height, setPlayer2Height] = useState("70%")
    const [finalScore, setFinalScore] = useState(null);

    useEffect(() => {
        // If coming from practice, update player1Height and finalScore
        if (location.state && location.state.finalScore !== undefined) {
            setFinalScore(location.state.finalScore);
            setPlayer1Height(`${Math.round(location.state.finalScore)}%`);
        }
    }, [location.state]);

    useEffect(() => {
        // set player heights (scores) to useState values
        const determineWinner = () => {
            try {
                if (parseFloat(player1Height) > parseFloat(player2Height)) {
                    setEndingMessage("you won!")
                } else if (parseFloat(player1Height) < parseFloat(player2Height)) {
                    setEndingMessage("you lost :(")
                } else {
                    setEndingMessage("it's a tie... better practice more!")
                }
            } catch (error) {
                console.error("Error fetching results", error);
            }
        };

        if (player1Height != null && player2Height != null) {
            determineWinner();
        }
    }, [player1Height, player2Height]);

    

    return (
        <>
            <div 
                className="results-background"
                style={{
                    backgroundImage:`url(${resultsBackground})`,
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
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'flex-end',
                    padding: '2rem'
                }}
            >
                <div className="podiums-container">
                    <div className="player1-results">
                        <div // this is just the podium box
                            className="podium-player1" 
                            style={{ '--podium1-height': player1Height }}
                        />
                        <h1 className="player1-accuracy-score">{finalScore !== null ? `${Math.round(finalScore)}%` : player1Height}</h1>
                        <img 
                            src={player1Sprite} 
                            className="player1-ending-sprite" 
                            alt="Player 1 sprite" 
                            style={{ bottom: player1Height }} 
                        />
                    </div>

                    <div className="player2-results">
                        <div // this is just the podium box
                            className="podium-player2" 
                            style={{ '--podium2-height': player2Height }}
                        />
                        <h1 className="player2-accuracy-score">{player2Height}</h1>
                        <img 
                            src={player2Sprite} 
                            className="player2-ending-sprite" 
                            alt="Player 2 sprite" 
                            style={{ bottom: player2Height }} 
                        />
                    </div>
                    


                </div>

                <div className="results-container">
                    <h1 className="ending-message">{endingMessage}</h1>
                    <button className="go-back" onClick={() => window.location.href = "/"}>back to title page</button> 
                </div>
            </div>
            
        </>
    )
}