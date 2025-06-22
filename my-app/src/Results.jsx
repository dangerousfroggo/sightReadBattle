import { useState, useEffect } from "react"

import resultsBackground from './assets/results_background.png'
import player2Sprite from './assets/player-2-sprite.png'
import player1Sprite from './assets/player-1-sprite.png'

export default function Results() {
    const [endingMessage, setEndingMessage] = useState("")
    const [player1Height, setPlayer1Height] = useState("50%") // Example heights, adjust as needed
    const [player2Height, setPlayer2Height] = useState("70%")
    
    useEffect(() => {
        // set player heights (scores) to useState values
        const determineWinner = () => {
            try {
                if (parseFloat(player1Height) > parseFloat(player2Height)) {
                    setEndingMessage("you win!")
                } else if (parseFloat(player1Height) < parseFloat(player2Height)) {
                    setEndingMessage("you lose :(")
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
                        <img 
                            src={player2Sprite} 
                            className="player2-ending-sprite" 
                            alt="Player 2 sprite" 
                            style={{ bottom: player2Height }} 
                        />
                    </div>
                    {/* <div className="player1-results" style={{ '--podium1-height': player1Height }}>
                        <div className="podium-player1" />
                        <img src={player1Sprite} className="player1-ending-sprite" alt="Player 1 sprite" />
                    </div>

                    <div className="player2-results" style={{ '--podium2-height': player2Height }}>
                        <div className="podium-player2" />
                        <img src={player2Sprite} className="player2-ending-sprite" alt="Player 2 sprite" />
                    </div> */}


                </div>

                <div className="results-container">
                    <h1 className="ending-message">{endingMessage}</h1>
                    <button className="go-back" onClick={() => window.location.href = "/"}>back to title page</button> 
                </div>
            </div>
            
        </>
    )
}