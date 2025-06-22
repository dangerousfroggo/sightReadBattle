import { useState, useEffect } from "react"

import resultsBackground from './assets/results_background.png'
import player2Sprite from './assets/player-2-sprite.png'
import player1Sprite from './assets/player-1-sprite.png'

export default function Results() {
    const [endingMessage, setEndingMessage] = useState("")
    const [player1Height, setPlayer1Height] = useState("0%") // Example heights, adjust as needed
    const [player2Height, setPlayer2Height] = useState("70%")
    // const [finalScore, setFinalScore] = useState(null);

    
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

    useEffect(() => {
        const fetchScore = async () => {
            try {
                const res = await fetch("http://127.0.0.1:5000/final_score");
                const data = await res.json();
                console.log("Final score:", data); // 👈 will log the Python-calculated score
                console.log(data.score)
                const twoDecimalScore = parseFloat(data.score).toFixed(2); // Format to two decimal places
                setPlayer1Height(twoDecimalScore + "%"); // Assuming the score is a percentage
            } catch (error) {
                console.error("Error fetching score:", error);
            }

        };

        fetchScore();
    }, []);


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
                            style={{
                                '--podium1-height': `${parseFloat(player1Height) + 15}%`
                            }}
                        />
                        <h1 className="player1-accuracy-score">{player1Height}</h1>
                        <img 
                            src={player1Sprite} 
                            className="player1-ending-sprite" 
                            alt="Player 1 sprite"
                            style={{
                                bottom: `${parseFloat(player1Height) + 15}%` // Adjust the sprite position based on height
                            }}
                        />
                    </div>

                    {/* <div className="player2-results">
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
                    </div> */}

                </div>

                <div className="results-container">
                    {/* <h1 className="ending-message">{endingMessage}</h1> */}
                    <h1 className="ending-message">always room for improvement!</h1>
                    <button className="go-back" onClick={() => window.location.href = "/"}>back to title page</button> 
                </div>
            </div>
            
        </>
    )
}