import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import backgroundImage from './assets/upgraded_background_title.png'
import player1Sprite from './assets/player-1-sprite.png'


export default function Practice() {
    const [playerAccuracy, setPlayerAccuracy] = useState('0%');
    const [countdown, setCountdown] = useState(5);
    const [liveNote, setLiveNote] = useState('');
    const [liveRating, setLiveRating] = useState(0);
    const [finalScore, setFinalScore] = useState(null);
    const [sessionStarted, setSessionStarted] = useState(false);
    const [done, setDone] = useState(false);
    const navigate = useNavigate();

    // Countdown logic
    useEffect(() => {
        if (countdown > 0 && !sessionStarted) {
            const timer = setTimeout(() => setCountdown(countdown - 1), 1000);
            return () => clearTimeout(timer);
        } else if (countdown === 0 && !sessionStarted) {
            // Start backend session
            fetch('http://localhost:5000/start_practice', { method: 'POST' })
                .then(() => setSessionStarted(true));
        }
    }, [countdown, sessionStarted]);

    // Poll backend for live rating
    useEffect(() => {
        let interval;
        if (sessionStarted && !done) {
            interval = setInterval(() => {
                fetch('http://localhost:5000/live_rating')
                    .then(res => res.json())
                    .then(data => {
                        setLiveNote(data.current_note);
                        setLiveRating(data.current_rating);
                        setPlayerAccuracy(`${Math.round(data.current_rating)}%`);
                        setDone(data.done);
                        if (data.done) {
                            setFinalScore(data.final_score);
                            setTimeout(() => navigate('/results', { state: { finalScore: data.final_score } }), 2000);
                        }
                    });
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [sessionStarted, done, navigate]);

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
                    {countdown > 0 && !sessionStarted ? (
                        <div style={{ fontSize: '4rem', color: '#fff' }}>Starting in {countdown}...</div>
                    ) : (
                        <>
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
                            {/* this is where the sheet music will be displayed*/}
                        </div>
                        <div style={{ position: 'absolute', top: '2rem', left: '2rem', color: '#fff', fontSize: '2rem' }}>
                            {liveNote && <div>Current Note: {liveNote}</div>}
                            {liveRating !== null && <div>Live Rating: {liveRating}</div>}
                            {finalScore !== null && <div>Final Score: {finalScore}</div>}
                        </div>
                        </>
                    )}
                </div>
            </div>
        </>
    )
}
