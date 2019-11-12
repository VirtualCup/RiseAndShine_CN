from StringHelper import StringHelper;
from UnityFont import UnityFont;
from UnityText import UnityText;
import os, csv;

def gen_unity_font():
	# read text
	f = open("localization.new.csv", "rb");
	csv_reader = csv.reader(f);
	
	txts = "";
	for row in csv_reader:
		txts += row[2];
	f.close();

	sh = StringHelper();
	sh.code = "dos";
	sh.add_chars(txts.decode("utf-8"));
	sh.add_western();

	# Minify font
	strs = "\"" + sh.get_chars() + "\""
	tool_path = "\"E:\\Python Localization Helper\\Font\\sfnttool.jar\"";
	font_folder_path = "\"C:\\Windows\\Fonts\\{0}\"";
	font_export_folder_path = "\"Font\\{0}\"";
	
	commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("HappyFont.ttf"), font_export_folder_path.format("HappyFont.ttf")];
	os.system(" ".join(commandstr).encode('mbcs'));
	
	commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("xiaokou_NEW.ttf"), font_export_folder_path.format("XiaoDouNaoNao.ttf")];
	os.system(" ".join(commandstr).encode('mbcs'));

	# Gen Font
	font = UnityFont("OriginalFile/unnamed asset-resources.assets-403.dat", unity_version = [5, 4, 2, 2], version = 15);
	font.convert_to_raw("RiseAndShine/unnamed asset-resources.assets-403.dat", "Font/HappyFont.ttf");
	font = UnityFont("OriginalFile/unnamed asset-resources.assets-410.dat", unity_version = [5, 4, 2, 2], version = 15);
	font.convert_to_raw("RiseAndShine/unnamed asset-resources.assets-410.dat", "Font/XiaoDouNaoNao.ttf");

def gen_unity_text():
	uText = UnityText("OriginalFile/unnamed asset-resources.assets-395.dat");
	uText.load_from_txt("localization.new.csv");
	uText.save_to_raw("RiseAndShine/unnamed asset-resources.assets-395.dat")
	
gen_unity_font();
gen_unity_text();