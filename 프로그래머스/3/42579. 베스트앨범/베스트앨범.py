def solution(genres, plays):
    music = dict()
    play_per_genre = dict()
    for index, genre in enumerate(genres):
        music[genre] = music.get(genre, []) + [(index, plays[index])]
    for genre in genres:
        play_per_genre[genre] = sum([m[1] for m in music[genre]])
    sorted_genre = sorted(play_per_genre.items(), key = lambda x: x[1], reverse = True)
    
                    
    answer = []
    
    for genre, _ in sorted_genre:
        songs = sorted(music[genre], key = lambda x: (-x[1], x[0]))
        for song in songs[:2]:
            answer.append(song[0])

    return answer