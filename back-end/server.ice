module ApplicationArchitecturesDistribuees
{

	sequence<byte> byteList;

    interface Server
    {
        void helloWorld(string helloWorld);
		int getNewIndex();
		bool uploadPart(int id, byteList part);
		bool uploadFileAndInsertMusic(int id, string filename);
        void deleteMusic(string titleMusic);
        void searchMusic(string titleMusic);
        void updateMusicChangeTitle(string titleCurrent, string newTitle);
    }
}