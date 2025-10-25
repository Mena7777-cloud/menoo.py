import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="استمارة تدريب الحميدي",
    page_icon="📄",
    layout="centered"
)

# --- دالة لرسم خط فاصل ذهبي ---
def golden_line():
    """هذه الدالة ترسم خطًا أفقيًا ذهبيًا باستخدام HTML و CSS"""
    st.markdown("<hr style='border: none; height: 2px; background: linear-gradient(to left, #b8860b, #f0e68c); margin: 20px 0;'/>", unsafe_allow_html=True)

# --- دالة حفظ البيانات في Google Sheets (سنضيفها لاحقًا) ---
def save_to_sheets(data):
    # هذه الدالة ستحتوي على كود الاتصال بـ Google Sheets
    # سنكملها في الخطوة التالية بعد النشر
    st.error("لم يتم ربط قاعدة البيانات بعد. هذه رسالة اختبار.")
    return False

# --- العنوان الرئيسي ---
st.title("📄 استمارة تدريب في شركة الحميدي")
golden_line()

# --- بناء الاستمارة ---
with st.form(key="training_form", clear_on_submit=True):
    
    full_name = st.text_input("الاسم الكامل", placeholder="اكتب اسمك الثلاثي هنا")
    golden_line()

    email = st.text_input("البريد الإلكتروني", placeholder="example@email.com")
    golden_line()

    phone = st.text_input("رقم الهاتف", placeholder="01xxxxxxxxx")
    golden_line()

    national_id = st.text_input("الرقم القومي (14 رقم)", max_chars=14)
    golden_line()

    education = st.text_input("الجامعة / المؤهل الدراسي")
    golden_line()

    major = st.text_input("التخصص")
    golden_line()

    grad_year = st.number_input("سنة التخرج (المتوقعة)", min_value=2010, max_value=2030, step=1)
    golden_line()
    
    personal_photo = st.file_uploader("ارفع صورتك الشخصية هنا", type=['png', 'jpg', 'jpeg'])
    golden_line()
    
    id_photo = st.file_uploader("ارفع صورة البطاقة الشخصية (وجه أمامي)", type=['png', 'jpg', 'jpeg', 'pdf'])
    golden_line()
    
    why_training = st.text_area("لماذا ترغب في الحصول على هذا التدريب؟")
    golden_line()

    skills = st.text_area("ما هي أبرز المهارات التي تتقنها؟")
    golden_line()

    training_goal = st.text_area("ما هو هدفك الرئيسي من هذا التدريب؟")
    
    st.write("") 
    
    submitted = st.form_submit_button("إرسال الطلب الآن")

# --- ماذا يحدث بعد الضغط على الزر ---
if submitted:
    if not full_name or not email or not national_id:
        st.warning("يرجى ملء الحقول الأساسية: الاسم، البريد الإلكتروني، والرقم القومي.")
    else:
        # جمع البيانات في قاموس (Dictionary)
        data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "FullName": full_name,
            "Email": email,
            "Phone": phone,
            "NationalID": national_id,
            "Education": education,
            "Major": major,
            "GradYear": grad_year,
            "WhyTraining": why_training,
            "Skills": skills,
            "TrainingGoal": training_goal,
            "PersonalPhotoFile": personal_photo,
            "IDPhotoFile": id_photo
        }
        
        # محاولة حفظ البيانات
        if save_to_sheets(data):
            st.success(f"شكرًا لك، {full_name}! تم استلام طلبك بنجاح وحفظ بياناتك.")
            st.balloons()
        else:
            st.error("حدث خطأ أثناء محاولة حفظ البيانات. يرجى المحاولة مرة أخرى.")
