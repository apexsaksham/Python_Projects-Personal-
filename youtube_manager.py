import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_videos_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    if not videos:
        print("No videos available!")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Video: {video['name']}, Duration: {video['time']}")


def add_videos(videos):
    name = input("Enter the name of video: ")
    time = input("Enter the time of video: ")
    videos.append({"name": name, "time": time})
    save_videos_helper(videos)
    print("Video added successfully!")


def update_videos(videos):
    if not videos:
        print("No videos available to update!")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the number you want to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            videos[index - 1] = {"name": name, "time": time}
            save_videos_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_videos(videos):
    if not videos:
        print("No videos available to delete!")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the number you want to delete: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_videos_helper(videos)
            print("Video deleted successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()
