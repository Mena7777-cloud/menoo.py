import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="استمارة تدريب الحميدي",
    page_icon="📄",
    layout="centered"
)

# --- العنوان الرئيسي ---
st.title("📄 استمارة تدريب في شركة الحميدي")
st.write("---")

# --- بناء الاستمارة ---
with st.form(key="training_form", clear_on_submit=True):
    
    st.header("البيانات الشخصية")
    full_name = st.text_input("الاسم الكامل", placeholder="اكتب اسمك الثلاثي هنا")
    email = st.text_input("البريد الإلكتروني", placeholder="example@email.com")
    phone = st.text_input("رقم الهاتف", placeholder="01xxxxxxxxx")
    national_id = st.text_input("الرقم القومي (14 رقم)", max_chars=14)
    
    # --- حقول رفع الملفات الجديدة ---
    personal_photo = st.file_uploader("ارفع صورتك الشخصية هنا", type=['png', 'jpg', 'jpeg'])
    id_photo = st.file_uploader("ارفع صورة البطاقة الشخصية (وجه أمامي)", type=['png', 'jpg', 'jpeg', 'pdf'])
    
    st.write("---")
    
    st.header("المعلومات الأكاديمية")
    education = st.text_input("الجامعة / المؤهل الدراسي")
    major = st.text_input("التخصص")
    grad_year = st.number_input("سنة التخرج (المتوقعة)", min_value=2010, max_value=2030, step=1)
    
    st.write("---")

    st.header("أسئلة التقديم")
    why_training = st.text_area("لماذا ترغب في الحصول على هذا التدريب؟")
    skills = st.text_area("ما هي أبرز المهارات التي تتقنها؟")
    training_goal = st.text_area("ما هو هدفك الرئيسي من هذا التدريب؟")
    
    st.write("---")
    
    # زر الإرسال
    submitted = st.form_submit_button("إرسال الطلب الآن")

# --- ماذا يحدث بعد الضغط على الزر ---
if submitted:
    if not full_name or not email or not national_id:
        st.warning("يرجى ملء الحقول الأساسية: الاسم، البريد الإلكتروني، والرقم القومي.")
    else:
        # حاليًا، سنعرض رسالة نجاح ونؤكد استلام الملفات
        
        st.success(f"شكرًا لك، {full_name}! تم استلام طلبك بنجاح.")
        st.balloons()
        
        st.write("**ملخص البيانات التي تم إرسالها:**")
        st.write(f"- **الاسم:** {full_name}")
        st.write(f"- **البريد الإلكتروني:** {email}")
        
        # التأكد من أن الملفات تم رفعها قبل محاولة عرض أسمائها
        if personal_photo is not None:
            st.write(f"- **تم استلام الصورة الشخصية:** {personal_photo.name}")
        if id_photo is not None:
            st.write(f"- **تم استلام صورة البطاقة:** {id_photo.name}")
