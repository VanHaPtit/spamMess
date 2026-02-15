# import pandas as pd
# import joblib
# import os
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.pipeline import Pipeline
# from sklearn.svm import SVC
# from sklearn.naive_bayes import MultinomialNB

# # Đọc dữ liệu từ file bạn vừa clone về
# df = pd.read_csv(r'D:\Slide 28 tech\Kì 2 năm 4\Chuyên đề HTTT\spam_data.csv')
# X, y = df['text'].astype(str), df['label']

# # Đóng gói bộ chuyển đổi văn bản và thuật toán vào Pipeline
# model1 = Pipeline([('tfidf', TfidfVectorizer()), ('svc', SVC(kernel='linear'))])
# model2 = Pipeline([('tfidf', TfidfVectorizer()), ('nb', MultinomialNB())])

# print("--- Đang huấn luyện mô hình... ---")
# model1.fit(X, y)
# model2.fit(X, y)

# # Lưu vào thư mục Spam để views.py có thể tải lên
# os.makedirs('Spam', exist_ok=True)
# joblib.dump(model1, 'Spam/mySVCModel1.pkl')
# joblib.dump(model2, 'Spam/myModel.pkl')
# print("--- Đã hoàn thiện 2 file mô hình! ---")




import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

# 1. Cấu hình đường dẫn
BASE_DIR = r'D:\Slide 28 tech\Kì 2 năm 4\Chuyên đề HTTT'
EN_DATA = os.path.join(BASE_DIR, 'spam_data.csv')
VI_DATA = os.path.join(BASE_DIR, 'spamDataVN.csv')

def train_and_save_models():
    # 2. Đọc dữ liệu từ cả hai nguồn
    if not os.path.exists(EN_DATA) or not os.path.exists(VI_DATA):
        print("LỖI: Thiếu file dữ liệu (Anh hoặc Việt). Vui lòng chạy setup_data.py trước!")
        return

    print("--- Đang nạp dữ liệu song ngữ... ---")
    df_en = pd.read_csv(EN_DATA)
    df_vi = pd.read_csv(VI_DATA)

    # 3. Gộp dữ liệu
    df_combined = pd.concat([df_en, df_vi], ignore_index=True)
    
    # Loại bỏ các dòng trống để tránh lỗi Pipeline
    df_combined = df_combined.dropna(subset=['text', 'label'])
    
    X = df_combined['text'].astype(str)
    y = df_combined['label']

    print(f"Tổng mẫu huấn luyện: {len(df_combined)} (Anh: {len(df_en)}, Việt: {len(df_vi)})")

    # 4. Xây dựng Pipeline
    # TF-IDF giúp máy hiểu trọng số từ ngữ của cả 2 ngôn ngữ
    model1 = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2))), # Sử dụng cả từ đơn và từ ghép
        ('svc', SVC(kernel='linear', probability=True))
    ])

    model2 = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('nb', MultinomialNB())
    ])

    # 5. Huấn luyện
    print("--- Đang huấn luyện mô hình (có thể mất vài phút)... ---")
    model1.fit(X, y)
    model2.fit(X, y)

    # 6. Lưu mô hình vào thư mục dự án
    os.makedirs('Spam', exist_ok=True)
    joblib.dump(model1, 'Spam/mySVCModel1.pkl')
    joblib.dump(model2, 'Spam/myModel.pkl')
    
    print("--- CHÚC MỪNG: Đã hoàn thiện 2 file mô hình song ngữ! ---")

if __name__ == "__main__":
    train_and_save_models()








    # cách chạy code 
    # python setup_data.py
    # python train_system.py
    # python manage.py runserver