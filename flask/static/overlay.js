const homeScore = document.getElementById('home-score')
const visitorScore = document.getElementById('visitor-score')
const gameClock = document.getElementById('game-clock')
const shotClock = document.getElementById('shot-clock')
const period = document.getElementById('period')

const homeSummaryScore = document.getElementById('home-summary-score')
const visitorSummaryScore = document.getElementById('visitor-summary-score')
const summaryTag = document.getElementById('summary-tag')

const scorebox = document.getElementById('scorebox')

const scorestate = document.getElementById('scorestate')

const socket = io()

socket.on('update', payload => {
    homeScore.innerText = payload.home_score
    visitorScore.innerText = payload.visitor_score
    gameClock.innerText = payload.clock
    shotClock.innerText = payload.shot
    period.innerText = payload.period
})

socket.on('display_mode', payload => {
    console.log(payload)
    if (payload.mode == 'live')
    {
        scorebox.classList.remove('hide')
        scorestate.classList.add('hide')
    }
    else
    {
        homeSummaryScore.innerText = payload.home_score
        visitorSummaryScore.innerText = payload.visitor_score
        summaryTag.innerText = payload.tag
        scorebox.classList.add('hide')
        scorestate.classList.remove('hide')
    }
})
