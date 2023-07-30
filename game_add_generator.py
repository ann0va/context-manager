import csv

def read_scores_from_csv(filename):
    scores = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) 
        for row in csv_reader:
            player_name, score = row[0], int(row[1])
            scores.append((player_name, score))
    return scores

def find_highest_scores(scores):
    highest_scores = {}
    for player, score in scores:
        if player not in highest_scores or score > highest_scores[player]:
            highest_scores[player] = score
    return highest_scores

def save_high_scores_to_csv(high_scores):
    sorted_scores = sorted(high_scores.items(), key=lambda item: item[1], reverse=True)
    with open('high_scores.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Player name', 'Highest score'])
        csv_writer.writerows(sorted_scores)

if __name__ == "__main__":
    previous_scores = read_scores_from_csv('game_scores.csv')
    highest_scores = find_highest_scores(previous_scores)
    save_high_scores_to_csv(highest_scores)
