from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def text_summarization_english(text):
    # For Strings
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Summarize using sumy TextRank
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 2)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    return text_summary



def text_summarization_indonesian(teks, stopwords):
    stopwords = set(stopwords.words("indonesian"))
    words = word_tokenize(teks)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopwords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    # Creatinng a dictianary to keep the score
    sentences = sent_tokenize(teks)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (average)):
            summary += " " + sentence
    return summary



textEnglish = """A vaccine for the coronavirus will likely be ready by early 2021 but rolling it out safely across India’s 1.3 billion people will be the country’s biggest challenge in fighting its surging epidemic, a leading vaccine scientist told Bloomberg.
India, which is host to some of the front-runner vaccine clinical trials, currently has no local infrastructure in place to go beyond immunizing babies and pregnant women, said Gagandeep Kang, professor of microbiology at the Vellore-based Christian Medical College and a member of the WHO’s Global Advisory Committee on Vaccine Safety.
The timing of the vaccine is a contentious subject around the world. In the U.S., President Donald Trump has contradicted a top administration health expert by saying a vaccine would be available by October. In India, Prime Minister Narendra Modi’s government had promised an indigenous vaccine as early as mid-August, a claim the government and its apex medical research body has since walked back.
"""

summaryEnglish = text_summarization_english(textEnglish)
print("English Text")
print("Total Karakter : " , len(textEnglish))
print(summaryEnglish)
print("Total Karakter : " , len(summaryEnglish))


teksIndonesia = """Komisi Pemberantasan Korupsi (KPK) memastikan akan melantik 1.271 pegawai KPK menjadi aparatur sipil negara (ASN). “Pelantikan akan diikuti oleh 1.271 pegawai secara daring dan luring di Aula Gedung Juang KPK,” kata Pelaksana Tugas Juru Bicara KPK Ali Fikri, Senin (31/5/2021) malam. Ali menyebutkan, pelantikan dilaksanakan pada pukul 13.00 WIB. Namun, untuk memastikan penerapan protokol kesehatan, yang hadir secara langsung hanya 53 perwakilan pegawai dan pejabat struktural. “Selebihnya pegawai mengikuti pelantikan melalui aplikasi daring dan wajib melakukan absensi serta menunjukkan bukti kehadiran,” ucap Ali. Adapun rangkaian pelantikan terdiri dari Pelantikan dan Pengambilan Sumpah/Janji PNS dan Sumpah/Janji Jabatan Pimpinan Tinggi Madya; Jabatan Pimpinan Tinggi Pratama dan Administrator. Terima kasih telah membaca Kompas.com. Dapatkan informasi, inspirasi dan insight di email kamu. “KPK akan menyiarkan seluruh rangkaian kegiatan ini secara langsung melalui kanal YouTube KPK,” ucap dia. Sebelumnya, Kepala Badan Kepegawaian Negara (BKN) Bima Haria Wibisana juga telah menerima undangan pelantikan pegawai KPK menjadi ASN besok. “Saya dapat undangan pelantikan besok jam 14.00,” kata Bima kepada Kompas.com, Senin (31/5/2021). Sebelumnya, Wakil Ketua KPK Nurul Ghufron menyatakan bahwa pimpinan KPK akan mengadakan rapat perihal adanya surat mengenai usulan permintaan penundaan pelantikan pegawai KPK pada hari ini. Adapun surat itu dikirim oleh pegawai KPK yang lolos tes wawasan kebangsaan dan menilai hasil TWK masih bermasalah. "Rencananya akan kami bahas Senin, hasilnya kami kabarkan selanjutnya," ucap Ghufron dalam keterangan tertulis, Minggu (30/5/2021). Ghufron menilai, pimpinan KPK menghargai sikap para pegawai yang bersolidaritas dengan 75 pegawai lain yang tak lolos TWK. Menurut dia, solidaritas pegawai KPK yang meminta penundaan tersebut merupakan pengamalan dari sila Pancasila tentang Persatuan Indonesia. 
"Solidaritas dari segenap pegawai KPK yang meminta agar pelantikan ditunda sangat kami hargai," kata Ghufron. Ia pun mengungkapkan alasan menjadikan tanggal 1 Juni 2021 sebagai hari pelantikan pegawai KPK menjadi ASN. Ghufron menyebut, pimpinan KPK memilih pelantikan yang bertepatan pada hari lahir Pancasila itu sebagai simbol bahwa pegawai KPK adalah seorang Pancasilais. "Untuk memperingati dan menghormati Hari Lahir Pancasila, sehingga secara simbolik untuk menyatakan bahwa pegawai KPK Pancasilais," kata dia. Hampir 700 pegawai Komisi Pemberantasan Korupsi (KPK) yang berasal dari berbagai direktorat mengirimkan surat terbuka kepada pimpinan KPK. Mereka meminta agar pelantikan sebagai ASN ditunda, di tengah polemik 75 pegawai yang tidak lolos TWK. Ada dugaan bahwa 75 pegawai itu tak lolos TWK sebagai upaya penyingkiran dan pelemahan terhadap KPK. Dari 75 pegawai yang dinyatakan tidak lolos TWK tersebut, 51 di antaranya diberhentikan dan 24 pegawai akan dibina kembali. Tidak hanya itu, materi TWK juga dianggap bermasalah, dinilai melecehkan perempuan hingga bertentangan dengan hak asasi manusia.
"""
summaryIndonesian = text_summarization_indonesian(teksIndonesia, stopwords)
print("\nIndonesian Text")
print("Total Karakter : " ,  len(teksIndonesia))
print(summaryIndonesian)
print("Total Karakter : " ,  len(summaryIndonesian))
