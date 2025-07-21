# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, ConversationHandler
# import logging

# # TOKEN ni to'g'ridan-to'g'ri shu yerga kiriting
# TOKEN = "7890497579:AAEccjVmmlMdfac3nC6V0tMB-PApFGn9ydo"  # @BotFather dan olingan tokeni shu yerga yozing

# # Admin IDs (bu yerga adminlarning Telegram ID larini qo'shing)
# ADMIN_IDS = [7592352824]  # Bu joyga adminlarning Telegram ID raqamlari qo'yiladi

# # Logging sozlamalari
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Suhbat bosqichlari
# TILNI_TANLASH, ISMNI_OLISH, RAQAMNI_OLISH, XIZMATNI_TANLASH, BUYURTMA_BERISH = range(5)

# # Til ma'lumotlari lug'ati
# texts = {
#     'uz': {
#         'greeting': "Assalomu alaykum, {}! 👋\n\n<b>Astris Media</b> rasmiy botiga xush kelibsiz! 🚀\n\nBizning xizmatlarimiz:\n• SMM\n• Target\n• Influencer marketing\n• Shaxsiy brend yaratish\n• Smm strategiya + kontent plan yaratish\n\nQuyidagi menyudan kerakli bo'limni tanlang:",
#         'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#         'services_button': "ℹ️ Xizmatlar",
#         'prices_button': "💵 Narxlar",
#         'back_button': "◀️ Ortga",
#         'order_button': "🗓 Bepul konsultatsiya uchun buyurtma qoldirish",
#         'contact_button': "✉️ Admin bilan bog'lanish",
#         'services_title': "<b>Bizning xizmatlarimiz:</b>\n\n",
#         'services_info': "<b>1. SMM </b>\nIjtimoiy tarmoqlarda brandni strategik rivojlantirish(Full komanda bilan)\n\n<b>2. Target </b>\nIjtimoiy tarmoqlarda brendingizni aniq auditoriyaga yo'naltirib, samarali reklama qilish.(2yillik tajribaga ega targetologlar bilan)\n\n<b>3. Shaxsiy brand</b>\nIjtimoiy tarmoqlarda imijingizni yaratish va strategik rivojlantirish (Full komanda bilan)\n\n<b>4. Influencer marketing</b>\nBrandingizni liderlar bilan birga tanitish(budjetdan kelib chiqqan holda)\n\n<b>5. Strategiya + Kontent plan</b>\nBrandingizni poydevorini mustahkamlash uchun oylik smm strategiya va shu asosida to'liq kontent plan(2 yillik yirik brandlar tajribasiga ega smm manager bilan)",
#         'prices_title': "<b>Xizmatlarimiz narxlari:</b>\n\n",
#         'prices_info': "<b>SMM uchun to'liq mas'uliyat va to'liq komanda bilan:</b>\n800$ - 1200$/oy\n\n<b>Target - 2 yillik tajribaga ega targetologlar bilan:</b>\n150$/oy\n\n<b>Influencer marketing:</b>\n• Mikro-influencerlar:  150$\n• Makro-influencerlar:  200$\n\n<b>Shaxsiy brend:</b>\n500$-1000$/oy\n\n<b>Strategiya + kontent plan:</b>\n2 yillik yirik brandlar tajribasiga ega smm manager bilan 150$/oy\n\nAniq narxlar xizmat ko'lami va murakkabligiga qarab o'zgarishi mumkin. Batafsil ma'lumot uchun admin bilan bog'laning.",
#         'order_start': "Buyurtma qoldirish uchun quyidagi ma'lumotlarni kiritishingiz kerak.\n\nAvval, ismingizni kiriting:",
#         'ask_phone': "Telefon raqamingizni kiriting (masalan: +998500786258):",
#         'ask_service': "Qaysi xizmat turi siz qiziqtiradi?",
#         'ask_details': "Buyurtmangiz haqida qo'shimcha ma'lumot kiriting:\nBiznesingiz haaqida qisqacha yozib qoldiring. Qanday natija xohlaysiz? Qaysi ijtimoiy tarmoqlar?",
#         'order_confirmation': "Buyurtmangiz qabul qilindi! ✅\n\n<b>Ism:</b> {}\n<b>Telefon:</b> {}\n<b>Xizmat turi:</b> {}\n<b>Qo'shimcha ma'lumot:</b> {}\n\nTez orada operatorlarimiz siz bilan bog'lanishadi. Rahmat!",
#         'contact_info': "Admin bilan bog'lanish uchun:\n\n📞 Telefon: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nYoki quyidagi tugmalardan foydalaning:",
#         'cancel_order': "Buyurtma bekor qilindi.",
#         'unknown_command': "Tushunarsiz buyruq. Iltimos, menyudan foydalaning.",
#         'new_order_admin': "🔔 <b>YANGI BUYURTMA!</b> 🔔\n\n<b>Ism:</b> {}\n<b>Telefon:</b> {}\n<b>Xizmat turi:</b> {}\n<b>Qо'shimcha ma'lumot:</b> {}\n\n<b>Chat ID:</b> {}",
#         'services': {
#             'smm': "SMM boshqaruv",
#             'target': "Target reklama",
#             'influencer': "Influencer marketing",
#             'brand': "Shaxsiy brend",
#             'content': "Kontent strategiya"
#         }
#     },
#     'ru': {
#         'greeting': "Здравствуйте, {}! 👋\n\nДобро пожаловать в официальный бот <b>Astris Media</b>! 🚀\n\nНаши услуги:\n• SMM\n• Таргет реклама\n• Influencer marketing\n• Создание персонального бренда\n• SMM стратегия + контент план\n\nВыберите нужный раздел из меню ниже:",
#         'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#         'services_button': "ℹ️ Услуги",
#         'prices_button': "💵 Цены",
#         'order_button': "🗓 Оставить заявку на бесплатную консультацию",
#         'contact_button': "✉️ Связаться с администратором",
#         'back_button': "◀️ Назад",
#         'services_title': "<b>Наши услуги:</b>\n\n",
#         'services_info': "<b>1. SMM </b>\nСтратегическое развитие бренда в социальных сетях (с полной командой)\n\n<b>2. Таргет реклама </b>\nЭффективная реклама вашего бренда для точной аудитории в социальных сетях (с таргетологами с 2-летним опытом)\n\n<b>3. Личный бренд</b>\nСоздание и стратегическое развитие вашего имиджа в социальных сетях (с полной командой)\n\n<b>4. Influencer marketing</b>\nПродвижение вашего бренда с лидерами мнений (в зависимости от бюджета)\n\n<b>5. Стратегия + Контент план</b>\nУкрепление фундамента вашего бренда с помощью ежемесячной SMM стратегии и полного контент-плана (с SMM менеджером с 2-летним опытом работы с крупными брендами)",
#         'prices_title': "<b>Цены на наши услуги:</b>\n\n",
#         'prices_info': "<b>SMM с полной ответственностью и полной командой:</b>\n800$ - 1200$/месяц\n\n<b>Таргет реклама - с таргетологами с 2-летним опытом:</b>\n150$/месяц\n\n<b>Influencer marketing:</b>\n• Микро-инфлюенсеры: 150$\n• Макро-инфлюенсеры: 200$\n\n<b>Личный бренд:</b>\n500$-1000$/месяц\n\n<b>Стратегия + контент план:</b>\nС SMM менеджером с 2-летним опытом работы с крупными брендами 150$/месяц\n\nТочные цены могут меняться в зависимости от объема и сложности услуг. Для подробной информации свяжитесь с администратором.",
#         'order_start': "Для оформления заявки вам необходимо предоставить следующую информацию.\n\nСначала введите ваше имя:",
#         'ask_phone': "Введите ваш номер телефона (например: +998500786258):",
#         'ask_service': "Какая услуга вас интересует?",
#         'ask_details': "Введите дополнительную информацию о вашем заказе:\nКратко опишите ваш бизнес. Каких результатов вы хотите достичь? Какие социальные сети?",
#         'order_confirmation': "Ваш заказ принят! ✅\n\n<b>Имя:</b> {}\n<b>Телефон:</b> {}\n<b>Тип услуги:</b> {}\n<b>Дополнительная информация:</b> {}\n\nНаши операторы свяжутся с вами в ближайшее время. Спасибо!",
#         'contact_info': "Для связи с администратором:\n\n📞 Телефон: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nИли используйте следующие кнопки:",
#         'cancel_order': "Заказ отменен.",
#         'unknown_command': "Непонятная команда. Пожалуйста, используйте меню.",
#         'new_order_admin': "🔔 <b>НОВЫЙ ЗАКАЗ!</b> 🔔\n\n<b>Имя:</b> {}\n<b>Телефон:</b> {}\n<b>Вид услуги:</b> {}\n<b>Дополнительная информация:</b> {}\n\n<b>Chat ID:</b> {}",
#         'services': {
#             'smm': "SMM управление",
#             'target': "Таргет реклама",
#             'influencer': "Influencer marketing",
#             'brand': "Личный бренд",
#             'content': "Контент стратегия"
#         }
#     },
#     'en': {
#         'greeting': "Hello, {}! 👋\n\nWelcome to the official <b>Astris Media</b> bot! 🚀\n\nOur services:\n• SMM\n• Target advertising\n• Influencer marketing\n• Personal brand creation\n• SMM strategy + content plan creation\n\nPlease select a section from the menu below:",
#         'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#         'services_button': "ℹ️ Services",
#         'prices_button': "💵 Prices",
#         'order_button': "🗓 Request a free consultation",
#         'contact_button': "✉️ Contact admin",
#         'back_button': "◀️ Back",
#         'services_title': "<b>Our services:</b>\n\n",
#         'services_info': "<b>1. SMM </b>\nStrategic brand development on social media (with a full team)\n\n<b>2. Target Advertising </b>\nEffective advertising of your brand to a precise audience on social media (with targeting specialists with 2 years of experience)\n\n<b>3. Personal brand</b>\nCreating and strategically developing your image on social media (with a full team)\n\n<b>4. Influencer marketing</b>\nPromoting your brand with opinion leaders (depending on budget)\n\n<b>5. Strategy + Content plan</b>\nStrengthening your brand's foundation with monthly SMM strategy and a complete content plan (with an SMM manager with 2 years of experience with major brands)",
#         'prices_title': "<b>Our service prices:</b>\n\n",
#         'prices_info': "<b>SMM with full responsibility and a complete team:</b>\n$800 - $1200/month\n\n<b>Target advertising - with targeting specialists with 2 years of experience:</b>\n$150/month\n\n<b>Influencer marketing:</b>\n• Micro-influencers: $150\n• Macro-influencers: $200\n\n<b>Personal brand:</b>\n$500-$1000/month\n\n<b>Strategy + content plan:</b>\nWith an SMM manager with 2 years of experience with major brands $150/month\n\nExact prices may vary depending on the scope and complexity of services. Contact the administrator for detailed information.",
#         'order_start': "To submit an order, you need to provide the following information.\n\nFirst, enter your name:",
#         'ask_phone': "Enter your phone number (for example: +998500786258):",
#         'ask_service': "Which service are you interested in?",
#         'ask_details': "Enter additional information about your order:\nBriefly describe your business. What results do you want to achieve? Which social networks?",
#         'order_confirmation': "Your order has been accepted! ✅\n\n<b>Name:</b> {}\n<b>Phone:</b> {}\n<b>Service type:</b> {}\n<b>Additional information:</b> {}\n\nOur operators will contact you soon. Thank you!",
#         'contact_info': "To contact the administrator:\n\n📞 Phone: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nOr use the following buttons:",
#         'cancel_order': "Order canceled.",
#         'unknown_command': "Unknown command. Please use the menu.",
#         'new_order_admin': "🔔 <b>NEW ORDER!</b> 🔔\n\n<b>Name:</b> {}\n<b>Phone:</b> {}\n<b>Service type:</b> {}\n<b>Additional information:</b> {}\n\n<b>Chat ID:</b> {}",
#         'services': {
#             'smm': "SMM management",
#             'target': "Target advertising",
#             'influencer': "Influencer marketing",
#             'brand': "Personal brand",
#             'content': "Content strategy"
#         }
#     }
# }

# # Til menyusi tugmalari
# def language_keyboard():
#     keyboard = [
#         [InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz")],
#         [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
#         [InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")]
#     ]
#     return InlineKeyboardMarkup(keyboard)

# # Asosiy menyu tugmalari
# def main_menu_keyboard(lang):
#     keyboard = [
#         [KeyboardButton(texts[lang]['services_button'])],
#         [KeyboardButton(texts[lang]['prices_button'])],
#         [KeyboardButton(texts[lang]['order_button'])],
#         [KeyboardButton(texts[lang]['contact_button'])]
#     ]
#     return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
# def back_keyboard(lang):
#     """Ortga tugmasi bilan inline keyboard"""
#     keyboard = [
#         [InlineKeyboardButton(texts[lang]['back_button'], callback_data="back_to_menu")]
#     ]
#     return InlineKeyboardMarkup(keyboard)


# # Start buyrug'i - tilni tanlash uchun
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text(
#         "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#         reply_markup=language_keyboard()
#     )
#     return TILNI_TANLASH

# # Tilni qayta ishlash
# async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()
    
#     lang = query.data.replace("lang_", "")
#     context.user_data["language"] = lang
    
#     user = update.effective_user
    
#     await query.message.reply_html(
#         texts[lang]['greeting'].format(user.first_name),
#         reply_markup=main_menu_keyboard(lang)
#     )
    
#     return ConversationHandler.END

# # Til o'zgartirishni qayta boshlash
# async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text(
#         "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#         reply_markup=language_keyboard()
#     )
#     return TILNI_TANLASH

# # Xizmatlar bo'limi
# async def services(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     lang = context.user_data.get("language", "uz")
    
#     await update.message.reply_html(
#         texts[lang]['services_title'] + texts[lang]['services_info'],
#         reply_markup=back_keyboard(lang)
#     )

# # Narxlar bo'limi
# async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     lang = context.user_data.get("language", "uz")
    
#     await update.message.reply_html(
#         texts[lang]['prices_title'] + texts[lang]['prices_info'],
#         reply_markup=back_keyboard(lang)
#     )

# # Buyurtma qoldirish
# async def order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     lang = context.user_data.get("language", "uz")
#     logger.info(f"Buyurtma berish boshlandi, til: {lang}")
    
#     await update.message.reply_html(
#         texts[lang]['order_start'],
#         reply_markup=None
#     )
#     return ISMNI_OLISH

# async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data["ism"] = update.message.text
#     lang = context.user_data.get("language", "uz")
#     logger.info(f"Ism olindi: {update.message.text}")
    
#     await update.message.reply_text(
#         texts[lang]['ask_phone']
#     )
#     return RAQAMNI_OLISH

# async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     phone = update.message.text
#     context.user_data["telefon"] = phone
#     lang = context.user_data.get("language", "uz")
    
#     # Xizmat turlarini tanlash uchun keyboard
#     keyboard = [
#         [InlineKeyboardButton("SMM", callback_data="service_smm")],
#         [InlineKeyboardButton(texts[lang]['services']['target'], callback_data="service_target")],
#         [InlineKeyboardButton("Influencer marketing", callback_data="service_influencer")],
#         [InlineKeyboardButton(texts[lang]['services']['brand'], callback_data="service_brand")],
#         [InlineKeyboardButton(texts[lang]['services']['content'], callback_data="service_content")]
#     ]
    
#     await update.message.reply_text(
#         texts[lang]['ask_service'],
#         reply_markup=InlineKeyboardMarkup(keyboard)
#     )
#     return XIZMATNI_TANLASH

# async def select_service(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()
    
#     service_type = query.data.replace("service_", "")
#     lang = context.user_data.get("language", "uz")
    
#     context.user_data["xizmat"] = texts[lang]['services'].get(service_type, "Unknown")
    
#     # Buyurtma haqida qo'shimcha ma'lumot so'rash
#     await query.message.reply_text(
#         texts[lang]['ask_details']
#     )
#     return BUYURTMA_BERISH

# async def process_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data["qoshimcha"] = update.message.text
#     lang = context.user_data.get("language", "uz")
    
#     # Foydalanuvchiga xabar yuborish
#     await update.message.reply_html(
#         texts[lang]['order_confirmation'].format(
#             context.user_data['ism'],
#             context.user_data['telefon'],
#             context.user_data['xizmat'],
#             context.user_data['qoshimcha']
#         ),
#         reply_markup=main_menu_keyboard(lang)
#     )
    
#     # Chat ID ni olish
#     chat_id = update.effective_chat.id
    
#     # Adminlarga bildirishnoma yuborish (har doim o'zbek tilida)
#     admin_message = texts['uz']['new_order_admin'].format(
#         context.user_data['ism'],
#         context.user_data['telefon'],
#         context.user_data['xizmat'],
#         context.user_data['qoshimcha'],
#         chat_id
#     )
    
#     for admin_id in ADMIN_IDS:
#         try:
#             await context.bot.send_message(
#                 chat_id=admin_id,
#                 text=admin_message,
#                 parse_mode="HTML"
#             )
#         except Exception as e:
#             logger.error(f"Admin {admin_id}ga xabar yuborishda xatolik: {e}")
    
#     return ConversationHandler.END

# # Buyurtma qoldirish yo'li
# async def order_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Buyurtma jarayonini boshlash uchun maxsus handler"""
#     return await order(update, context)

# # Admin bilan bog'lanish
# async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     lang = context.user_data.get("language", "uz")
    
#     keyboard = [
#         [InlineKeyboardButton("Instagram", url="https://www.instagram.com/astris_media?igsh=NTJjMHBjbW91cnQ0")],
#         [InlineKeyboardButton("Telegram", url="https://t.me/astrismedia")],
#         [InlineKeyboardButton(texts[lang]['back_button'], callback_data="back_to_menu")]
#     ]
    
#     await update.message.reply_html(
#         texts[lang]['contact_info'],
#         reply_markup=InlineKeyboardMarkup(keyboard)
#     )

# async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Ortga tugmasi bosilganda asosiy menyuga qaytish"""
#     query = update.callback_query
#     await query.answer()
    
#     lang = context.user_data.get("language", "uz")
#     user = update.effective_user
    
#     await query.message.reply_html(
#         texts[lang]['greeting'].format(user.first_name),
#         reply_markup=main_menu_keyboard(lang)
#     )
    
#     # Eski xabarni o'chirish
#     try:
#         await query.message.delete()
#     except:
#         pass

# # Xatoliklani qayta ishlash
# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     lang = context.user_data.get("language", "uz")
    
#     await update.message.reply_text(
#         texts[lang]['cancel_order'],
#         reply_markup=main_menu_keyboard(lang)
#     )
#     return ConversationHandler.END

# # Bu funktsiya error hatolikni oldini olish uchun qo'shildi
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Tanlanmagan menyular uchun xatolikni qayta ishlash"""
#     lang = context.user_data.get("language", "uz")
#     if not lang:  # Agar foydalanuvchi til tanlamaganini tekshiramiz
#         await update.message.reply_text(
#             "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
#             reply_markup=language_keyboard()
#         )
#         return
    
#     # Notanish xabar kelib qolsa
#     await update.message.reply_text(
#         texts[lang]['unknown_command'],
#         reply_markup=main_menu_keyboard(lang)
#     )

# def main() -> None:
#     # Botni yaratish va sozlash
#     application = Application.builder().token(TOKEN).build()

#     # Conversation handlerlar uchun alohida command handler qo'shish
#     application.add_handler(CommandHandler("order", order_command))
    
#     # Buyurtma qoldirish conversation handler
#     order_conv_handler = ConversationHandler(
#         entry_points=[
#             MessageHandler(
#                 filters.Regex(r"🗓.*консультаци.*|🗓.*consultation.*|🗓.*konsultatsiya.*"), 
#                 order
#             ),
#             CommandHandler("order", order_command)
#         ],
#         states={
#             ISMNI_OLISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
#             RAQAMNI_OLISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
#             XIZMATNI_TANLASH: [CallbackQueryHandler(select_service, pattern=r"^service_")],
#             BUYURTMA_BERISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_order)]
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#         name="order_conversation",
#         persistent=False
#     )
#     application.add_handler(order_conv_handler)
    
#     # Til tanlash conversation handler
#     lang_conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             TILNI_TANLASH: [CallbackQueryHandler(language_callback, pattern=r"^lang_")]
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#         name="language_selection",
#     )
#     application.add_handler(lang_conv_handler)

#     # Til o'zgartirish conversation handler
#     change_lang_handler = ConversationHandler(
#         entry_points=[
#             CommandHandler("language", change_language),
#             CommandHandler("til", change_language),
#             CommandHandler("yazyk", change_language)
#         ],
#         states={
#             TILNI_TANLASH: [CallbackQueryHandler(language_callback, pattern=r"^lang_")]
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#         name="change_language",
#     )
#     application.add_handler(change_lang_handler)
    
#     # Ortga qaytish uchun callback handler
#     application.add_handler(CallbackQueryHandler(back_to_menu, pattern=r"^back_to_menu$"))
    
#     # Xizmatlar uchun handler - REGEX PATTERN TUZATILDI
#     application.add_handler(MessageHandler(
#         filters.Regex(r"ℹ️.*[Xx]izmatlar|ℹ️.*Услуги|ℹ️.*Services"), 
#         services
#     ))
    
#     # Narxlar uchun handler - REGEX PATTERN TUZATILDI
#     application.add_handler(MessageHandler(
#         filters.Regex(r"💵.*[Nn]arxlar|💵.*Цены|💵.*Prices"), 
#         prices
#     ))
    
#     # Admin bilan bog'lanish - REGEX PATTERN TUZATILDI
#     application.add_handler(MessageHandler(
#         filters.Regex(r"✉️.*[Aa]dmin.*bog'lanish|✉️.*администратором|✉️.*[Cc]ontact.*admin"), 
#         contact_admin
#     ))
    
#     # Boshqa barcha xabarlar uchun handler
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     # Botni ishga tushirish
#     application.run_polling()

# if __name__ == "__main__":
#     main()





from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, ConversationHandler
import logging

# TOKEN ni to'g'ridan-to'g'ri shu yerga kiriting
TOKEN = "7890497579:AAEccjVmmlMdfac3nC6V0tMB-PApFGn9ydo"  # @BotFather dan olingan tokeni shu yerga yozing

# Admin IDs (bu yerga adminlarning Telegram ID larini qo'shing)
ADMIN_IDS = [7592352824]  # Bu joyga adminlarning Telegram ID raqamlari qo'yiladi

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Suhbat bosqichlari
TILNI_TANLASH, ISMNI_OLISH, RAQAMNI_OLISH, XIZMATNI_TANLASH, BUYURTMA_BERISH = range(5)

# Til ma'lumotlari lug'ati
texts = {
    'uz': {
        'greeting': "Assalomu alaykum, {}! 👋\n\n<b>Astris Media</b> rasmiy botiga xush kelibsiz! 🚀\n\nBizning xizmatlarimiz:\n• SMM\n• Target\n• Influencer marketing\n• Shaxsiy brend yaratish\n• Smm strategiya + kontent plan yaratish\n\nQuyidagi menyudan kerakli bo'limni tanlang:",
        'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
        'services_button': "ℹ️ Xizmatlar",
        'prices_button': "💵 Narxlar",
        'back_button': "◀️ Ortga",
        'order_button': "🗓 Bepul konsultatsiya uchun buyurtma qoldirish",
        'contact_button': "✉️ Admin bilan bog'lanish",
        'cancel_button': "❌ Bekor qilish",
        'services_title': "<b>Bizning xizmatlarimiz:</b>\n\n",
        'services_info': "<b>1. SMM </b>\nIjtimoiy tarmoqlarda brandni strategik rivojlantirish(Full komanda bilan)\n\n<b>2. Target </b>\nIjtimoiy tarmoqlarda brendingizni aniq auditoriyaga yo'naltirib, samarali reklama qilish.(2yillik tajribaga ega targetologlar bilan)\n\n<b>3. Shaxsiy brand</b>\nIjtimoiy tarmoqlarda imijingizni yaratish va strategik rivojlantirish (Full komanda bilan)\n\n<b>4. Influencer marketing</b>\nBrandingizni liderlar bilan birga tanitish(budjetdan kelib chiqqan holda)\n\n<b>5. Strategiya + Kontent plan</b>\nBrandingizni poydevorini mustahkamlash uchun oylik smm strategiya va shu asosida to'liq kontent plan(2 yillik yirik brandlar tajribasiga ega smm manager bilan)",
        'prices_title': "<b>Xizmatlarimiz narxlari:</b>\n\n",
        'prices_info': "<b>SMM uchun to'liq mas'uliyat va to'liq komanda bilan:</b>\n800$ - 1200$/oy\n\n<b>Target - 2 yillik tajribaga ega targetologlar bilan:</b>\n150$/oy\n\n<b>Influencer marketing:</b>\n• Mikro-influencerlar:  150$\n• Makro-influencerlar:  200$\n\n<b>Shaxsiy brend:</b>\n500$-1000$/oy\n\n<b>Strategiya + kontent plan:</b>\n2 yillik yirik brandlar tajribasiga ega smm manager bilan 150$/oy\n\nAniq narxlar xizmat ko'lami va murakkabligiga qarab o'zgarishi mumkin. Batafsil ma'lumot uchun admin bilan bog'laning.",
        'order_start': "Buyurtma qoldirish uchun quyidagi ma'lumotlarni kiritishingiz kerak.\n\nAvval, ismingizni kiriting:",
        'ask_phone': "Telefon raqamingizni kiriting (masalan: +998500786258):",
        'ask_service': "Qaysi xizmat turi siz qiziqtiradi?",
        'ask_details': "Buyurtmangiz haqida qo'shimcha ma'lumot kiriting:\nBiznesingiz haqida qisqacha yozib qoldiring. Qanday natija xohlaysiz? Qaysi ijtimoiy tarmoqlar?",
        'order_confirmation': "Buyurtmangiz qabul qilindi! ✅\n\n<b>Ism:</b> {}\n<b>Telefon:</b> {}\n<b>Xizmat turi:</b> {}\n<b>Qo'shimcha ma'lumot:</b> {}\n\nTez orada operatorlarimiz siz bilan bog'lanishadi. Rahmat!",
        'contact_info': "Admin bilan bog'lanish uchun:\n\n📞 Telefon: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nYoki quyidagi tugmalardan foydalaning:",
        'cancel_order': "Buyurtma bekor qilindi.",
        'unknown_command': "Tushunarsiz buyruq. Iltimos, menyudan foydalaning.",
        'new_order_admin': "🔔 <b>YANGI BUYURTMA!</b> 🔔\n\n<b>Ism:</b> {}\n<b>Telefon:</b> {}\n<b>Xizmat turi:</b> {}\n<b>Qо'shimcha ma'lumot:</b> {}\n\n<b>Chat ID:</b> {}",
        'select_language': "Tilni o'zgartirish uchun quyidagilardan birini tanlang:",
        'services': {
            'smm': "SMM boshqaruv",
            'target': "Target reklama",
            'influencer': "Influencer marketing",
            'brand': "Shaxsiy brend",
            'content': "Kontent strategiya"
        }
    },
    'ru': {
        'greeting': "Здравствуйте, {}! 👋\n\nДобро пожаловать в официальный бот <b>Astris Media</b>! 🚀\n\nНаши услуги:\n• SMM\n• Таргет реклама\n• Influencer marketing\n• Создание персонального бренда\n• SMM стратегия + контент план\n\nВыберите нужный раздел из меню ниже:",
        'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
        'services_button': "ℹ️ Услуги",
        'prices_button': "💵 Цены",
        'order_button': "🗓 Оставить заявку на бесплатную консультацию",
        'contact_button': "✉️ Связаться с администратором",
        'back_button': "◀️ Назад",
        'cancel_button': "❌ Отменить",
        'services_title': "<b>Наши услуги:</b>\n\n",
        'services_info': "<b>1. SMM </b>\nСтратегическое развитие бренда в социальных сетях (с полной командой)\n\n<b>2. Таргет реклама </b>\nЭффективная реклама вашего бренда для точной аудитории в социальных сетях (с таргетологами с 2-летним опытом)\n\n<b>3. Личный бренд</b>\nСоздание и стратегическое развитие вашего имиджа в социальных сетях (с полной командой)\n\n<b>4. Influencer marketing</b>\nПродвижение вашего бренда с лидерами мнений (в зависимости от бюджета)\n\n<b>5. Стратегия + Контент план</b>\nУкрепление фундамента вашего бренда с помощью ежемесячной SMM стратегии и полного контент-плана (с SMM менеджером с 2-летним опытом работы с крупными брендами)",
        'prices_title': "<b>Цены на наши услуги:</b>\n\n",
        'prices_info': "<b>SMM с полной ответственностью и полной командой:</b>\n800$ - 1200$/месяц\n\n<b>Таргет реклама - с таргетологами с 2-летним опытом:</b>\n150$/месяц\n\n<b>Influencer marketing:</b>\n• Микро-инфлюенсеры: 150$\n• Макро-инфлюенсеры: 200$\n\n<b>Личный бренд:</b>\n500$-1000$/месяц\n\n<b>Стратегия + контент план:</b>\nС SMM менеджером с 2-летним опытом работы с крупными брендами 150$/месяц\n\nТочные цены могут меняться в зависимости от объема и сложности услуг. Для подробной информации свяжитесь с администратором.",
        'order_start': "Для оформления заявки вам необходимо предоставить следующую информацию.\n\nСначала введите ваше имя:",
        'ask_phone': "Введите ваш номер телефона (например: +998500786258):",
        'ask_service': "Какая услуга вас интересует?",
        'ask_details': "Введите дополнительную информацию о вашем заказе:\nКратко опишите ваш бизнес. Каких результатов вы хотите достичь? Какие социальные сети?",
        'order_confirmation': "Ваш заказ принят! ✅\n\n<b>Имя:</b> {}\n<b>Телефон:</b> {}\n<b>Тип услуги:</b> {}\n<b>Дополнительная информация:</b> {}\n\nНаши операторы свяжутся с вами в ближайшее время. Спасибо!",
        'contact_info': "Для связи с администратором:\n\n📞 Телефон: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nИли используйте следующие кнопки:",
        'cancel_order': "Заказ отменен.",
        'unknown_command': "Непонятная команда. Пожалуйста, используйте меню.",
        'new_order_admin': "🔔 <b>НОВЫЙ ЗАКАЗ!</b> 🔔\n\n<b>Имя:</b> {}\n<b>Телефон:</b> {}\n<b>Вид услуги:</b> {}\n<b>Дополнительная информация:</b> {}\n\n<b>Chat ID:</b> {}",
        'select_language': "Выберите язык для изменения:",
        'services': {
            'smm': "SMM управление",
            'target': "Таргет реклама",
            'influencer': "Influencer marketing",
            'brand': "Личный бренд",
            'content': "Контент стратегия"
        }
    },
    'en': {
        'greeting': "Hello, {}! 👋\n\nWelcome to the official <b>Astris Media</b> bot! 🚀\n\nOur services:\n• SMM\n• Target advertising\n• Influencer marketing\n• Personal brand creation\n• SMM strategy + content plan creation\n\nPlease select a section from the menu below:",
        'language_select': "Iltimos, tilni tanlang / Please select a language / Пожалуйста, выберите язык",
        'services_button': "ℹ️ Services",
        'prices_button': "💵 Prices",
        'order_button': "🗓 Request a free consultation",
        'contact_button': "✉️ Contact admin",
        'back_button': "◀️ Back",
        'cancel_button': "❌ Cancel",
        'services_title': "<b>Our services:</b>\n\n",
        'services_info': "<b>1. SMM </b>\nStrategic brand development on social media (with a full team)\n\n<b>2. Target Advertising </b>\nEffective advertising of your brand to a precise audience on social media (with targeting specialists with 2 years of experience)\n\n<b>3. Personal brand</b>\nCreating and strategically developing your image on social media (with a full team)\n\n<b>4. Influencer marketing</b>\nPromoting your brand with opinion leaders (depending on budget)\n\n<b>5. Strategy + Content plan</b>\nStrengthening your brand's foundation with monthly SMM strategy and a complete content plan (with an SMM manager with 2 years of experience with major brands)",
        'prices_title': "<b>Our service prices:</b>\n\n",
        'prices_info': "<b>SMM with full responsibility and a complete team:</b>\n$800 - $1200/month\n\n<b>Target advertising - with targeting specialists with 2 years of experience:</b>\n$150/month\n\n<b>Influencer marketing:</b>\n• Micro-influencers: $150\n• Macro-influencers: $200\n\n<b>Personal brand:</b>\n$500-$1000/month\n\n<b>Strategy + content plan:</b>\nWith an SMM manager with 2 years of experience with major brands $150/month\n\nExact prices may vary depending on the scope and complexity of services. Contact the administrator for detailed information.",
        'order_start': "To submit an order, you need to provide the following information.\n\nFirst, enter your name:",
        'ask_phone': "Enter your phone number (for example: +998500786258):",
        'ask_service': "Which service are you interested in?",
        'ask_details': "Enter additional information about your order:\nBriefly describe your business. What results do you want to achieve? Which social networks?",
        'order_confirmation': "Your order has been accepted! ✅\n\n<b>Name:</b> {}\n<b>Phone:</b> {}\n<b>Service type:</b> {}\n<b>Additional information:</b> {}\n\nOur operators will contact you soon. Thank you!",
        'contact_info': "To contact the administrator:\n\n📞 Phone: +998 90 123 45 67\n✉️ Email: astrismedia1@gmail.com\n\nOr use the following buttons:",
        'cancel_order': "Order canceled.",
        'unknown_command': "Unknown command. Please use the menu.",
        'new_order_admin': "🔔 <b>NEW ORDER!</b> 🔔\n\n<b>Name:</b> {}\n<b>Phone:</b> {}\n<b>Service type:</b> {}\n<b>Additional information:</b> {}\n\n<b>Chat ID:</b> {}",
        'select_language': "Select a language to change:",
        'services': {
            'smm': "SMM management",
            'target': "Target advertising",
            'influencer': "Influencer marketing",
            'brand': "Personal brand",
            'content': "Content strategy"
        }
    }
}

# Til menyusi tugmalari
def language_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Asosiy menyu tugmalari
def main_menu_keyboard(lang):
    keyboard = [
        [KeyboardButton(texts[lang]['services_button'])],
        [KeyboardButton(texts[lang]['prices_button'])],
        [KeyboardButton(texts[lang]['order_button'])],
        [KeyboardButton(texts[lang]['contact_button'])]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Ortga tugmasi uchun keyboard
def back_keyboard(lang):
    keyboard = [
        [InlineKeyboardButton(texts[lang]['back_button'], callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Bekor qilish tugmasi
def cancel_keyboard(lang):
    keyboard = [
        [KeyboardButton(texts[lang]['cancel_button'])]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

# Start buyrug'i - tilni tanlash uchun
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Avvalgi ma'lumotlarni tozalash
    context.user_data.clear()
    
    await update.message.reply_text(
        texts['uz']['language_select'],
        reply_markup=language_keyboard()
    )
    return TILNI_TANLASH

# Tilni qayta ishlash
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    lang = query.data.replace("lang_", "")
    context.user_data["language"] = lang
    
    user = update.effective_user
    
    # Eski xabarni o'chirish
    try:
        await query.message.delete()
    except:
        pass
    
    await query.message.reply_html(
        texts[lang]['greeting'].format(user.first_name),
        reply_markup=main_menu_keyboard(lang)
    )
    
    return ConversationHandler.END

# Til o'zgartirishni qayta boshlash
async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    
    await update.message.reply_text(
        texts[lang]['select_language'],
        reply_markup=language_keyboard()
    )
    return TILNI_TANLASH

# Xizmatlar bo'limi
async def services(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = context.user_data.get("language", "uz")
    
    await update.message.reply_html(
        texts[lang]['services_title'] + texts[lang]['services_info'],
        reply_markup=back_keyboard(lang)
    )

# Narxlar bo'limi
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = context.user_data.get("language", "uz")
    
    await update.message.reply_html(
        texts[lang]['prices_title'] + texts[lang]['prices_info'],
        reply_markup=back_keyboard(lang)
    )

# Buyurtma qoldirish
async def start_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    logger.info(f"Buyurtma berish boshlandi, til: {lang}, user: {update.effective_user.id}")
    
    # Buyurtma ma'lumotlarini tozalash
    for key in ['ism', 'telefon', 'xizmat', 'qoshimcha']:
        if key in context.user_data:
            del context.user_data[key]
    
    await update.message.reply_html(
        texts[lang]['order_start'],
        reply_markup=cancel_keyboard(lang)
    )
    return ISMNI_OLISH

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Bekor qilish tugmasini tekshirish
    lang = context.user_data.get("language", "uz")
    if update.message.text == texts[lang]['cancel_button']:
        return await cancel_order(update, context)
    
    context.user_data["ism"] = update.message.text.strip()
    logger.info(f"Ism olindi: {update.message.text}")
    
    await update.message.reply_text(
        texts[lang]['ask_phone'],
        reply_markup=cancel_keyboard(lang)
    )
    return RAQAMNI_OLISH

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    
    # Bekor qilish tugmasini tekshirish
    if update.message.text == texts[lang]['cancel_button']:
        return await cancel_order(update, context)
    
    phone = update.message.text.strip()
    context.user_data["telefon"] = phone
    logger.info(f"Telefon olindi: {phone}")
    
    # Xizmat turlarini tanlash uchun keyboard
    keyboard = [
        [InlineKeyboardButton("SMM", callback_data="service_smm")],
        [InlineKeyboardButton(texts[lang]['services']['target'], callback_data="service_target")],
        [InlineKeyboardButton("Influencer marketing", callback_data="service_influencer")],
        [InlineKeyboardButton(texts[lang]['services']['brand'], callback_data="service_brand")],
        [InlineKeyboardButton(texts[lang]['services']['content'], callback_data="service_content")],
        [InlineKeyboardButton(texts[lang]['cancel_button'], callback_data="cancel_order")]
    ]
    
    await update.message.reply_text(
        texts[lang]['ask_service'],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return XIZMATNI_TANLASH

async def select_service(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    # Bekor qilish tugmasini tekshirish
    if query.data == "cancel_order":
        return await cancel_order_callback(update, context)
    
    service_type = query.data.replace("service_", "")
    lang = context.user_data.get("language", "uz")
    
    context.user_data["xizmat"] = texts[lang]['services'].get(service_type, "SMM")
    logger.info(f"Xizmat tanlandi: {context.user_data['xizmat']}")
    
    # Eski xabarni o'chirish
    try:
        await query.message.delete()
    except:
        pass
    
    # Buyurtma haqida qo'shimcha ma'lumot so'rash
    await query.message.reply_text(
        texts[lang]['ask_details'],
        reply_markup=cancel_keyboard(lang)
    )
    return BUYURTMA_BERISH

async def process_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    
    # Bekor qilish tugmasini tekshirish
    if update.message.text == texts[lang]['cancel_button']:
        return await cancel_order(update, context)
    
    context.user_data["qoshimcha"] = update.message.text.strip()
    logger.info(f"Buyurtma yakunlandi: {context.user_data}")
    
    # Foydalanuvchiga xabar yuborish
    await update.message.reply_html(
        texts[lang]['order_confirmation'].format(
            context.user_data.get('ism', 'N/A'),
            context.user_data.get('telefon', 'N/A'),
            context.user_data.get('xizmat', 'N/A'),
            context.user_data.get('qoshimcha', 'N/A')
        ),
        reply_markup=main_menu_keyboard(lang)
    )
    
    # Chat ID ni olish
    chat_id = update.effective_chat.id
    user = update.effective_user
    
    # Adminlarga bildirishnoma yuborish
    admin_message = texts['uz']['new_order_admin'].format(
        context.user_data.get('ism', 'N/A'),
        context.user_data.get('telefon', 'N/A'),
        context.user_data.get('xizmat', 'N/A'),
        context.user_data.get('qoshimcha', 'N/A'),
        chat_id
    )
    
    # User ma'lumotlarini ham qo'shish
    admin_message += f"\n<b>Username:</b> @{user.username if user.username else 'No'}"
    admin_message += f"\n<b>User ID:</b> {user.id}"
    admin_message += f"\n<b>First name:</b> {user.first_name}"
    admin_message += f"\n<b>Last name:</b> {user.last_name if user.last_name else 'No'}"
    
    for admin_id in ADMIN_IDS:
        try:
            await context.bot.send_message(
                chat_id=admin_id,
                text=admin_message,
                parse_mode="HTML"
            )
        except Exception as e:
            logger.error(f"Admin {admin_id}ga xabar yuborishda xatolik: {e}")
    
    return ConversationHandler.END

# Admin bilan bog'lanish
async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = context.user_data.get("language", "uz")
    
    keyboard = [
        [InlineKeyboardButton("Instagram", url="https://www.instagram.com/astris_media?igsh=NTJjMHBjbW91cnQ0")],
        [InlineKeyboardButton("Telegram", url="https://t.me/astrismedia")],
        [InlineKeyboardButton(texts[lang]['back_button'], callback_data="back_to_menu")]
    ]
    
    await update.message.reply_html(
        texts[lang]['contact_info'],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ortga tugmasi bosilganda asosiy menyuga qaytish"""
    query = update.callback_query
    await query.answer()
    
    lang = context.user_data.get("language", "uz")
    user = update.effective_user
    
    # Eski xabarni o'chirish
    try:
        await query.message.delete()
    except:
        pass
    
    await query.message.reply_html(
        texts[lang]['greeting'].format(user.first_name),
        reply_markup=main_menu_keyboard(lang)
    )

# Buyurtma bekor qilish (text message)
async def cancel_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    
    # Buyurtma ma'lumotlarini tozalash
    for key in ['ism', 'telefon', 'xizmat', 'qoshimcha']:
        if key in context.user_data:
            del context.user_data[key]
    
    await update.message.reply_text(
        texts[lang]['cancel_order'],
        reply_markup=main_menu_keyboard(lang)
    )
    return ConversationHandler.END

# Buyurtma bekor qilish (callback)
async def cancel_order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    lang = context.user_data.get("language", "uz")
    
    # Buyurtma ma'lumotlarini tozalash
    for key in ['ism', 'telefon', 'xizmat', 'qoshimcha']:
        if key in context.user_data:
            del context.user_data[key]
    
    # Eski xabarni o'chirish
    try:
        await query.message.delete()
    except:
        pass
    
    await query.message.reply_text(
        texts[lang]['cancel_order'],
        reply_markup=main_menu_keyboard(lang)
    )
    return ConversationHandler.END

# Umumiy cancel handler
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("language", "uz")
    
    await update.message.reply_text(
        texts[lang]['cancel_order'],
        reply_markup=main_menu_keyboard(lang)
    )
    return ConversationHandler.END

# Bu funktsiya error hatolikni oldini olish uchun
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Barcha xabarlarni qayta ishlash"""
    lang = context.user_data.get("language")
    
    # Agar til tanlanmagan bo'lsa, tilni tanlashga yo'naltirish
    if not lang:
        await update.message.reply_text(
            texts['uz']['language_select'],
            reply_markup=language_keyboard()
        )
        return
    
    message_text = update.message.text
    
    # Xizmatlar tugmasi
    if message_text == texts[lang]['services_button']:
        await services(update, context)
    
    # Narxlar tugmasi
    elif message_text == texts[lang]['prices_button']:
        await prices(update, context)
    
    # Buyurtma tugmasi
    elif message_text == texts[lang]['order_button']:
        await start_order(update, context)
    
    # Admin bilan bog'lanish tugmasi
    elif message_text == texts[lang]['contact_button']:
        await contact_admin(update, context)
    
    # Noma'lum buyruq
    else:
        await update.message.reply_text(
            texts[lang]['unknown_command'],
            reply_markup=main_menu_keyboard(lang)
        )

# Error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log error va foydalanuvchiga xabar berish."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    # Agar update mavjud bo'lsa va effective_message bor bo'lsa
    if isinstance(update, Update) and update.effective_message:
        try:
            lang = context.user_data.get("language", "uz")
            await update.effective_message.reply_text(
                "Xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring." if lang == 'uz' else 
                "Произошла ошибка. Пожалуйста, попробуйте еще раз." if lang == 'ru' else
                "An error occurred. Please try again."
            )
        except Exception as e:
            logger.error(f"Error handler xatoligi: {e}")

def main() -> None:
    """Botni ishga tushirish"""
    # Application yaratish
    application = Application.builder().token(TOKEN).build()
    
    # Conversation handler yaratish
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("lang", change_language),
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
        ],
        states={
            TILNI_TANLASH: [CallbackQueryHandler(language_callback, pattern="^lang_")],
            ISMNI_OLISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            RAQAMNI_OLISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            XIZMATNI_TANLASH: [CallbackQueryHandler(select_service, pattern="^(service_|cancel_)")],
            BUYURTMA_BERISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_order)]
        },
        fallbacks=[
            CommandHandler("cancel", cancel),
            MessageHandler(filters.Regex("^(❌ Bekor qilish|❌ Отменить|❌ Cancel)$"), cancel)
        ],
        allow_reentry=True
    )
    
    # Handler'larni qo'shish
    application.add_handler(conv_handler)
    
    # Callback query handler'lar
    application.add_handler(CallbackQueryHandler(back_to_menu, pattern="^back_to_menu$"))
    application.add_handler(CallbackQueryHandler(language_callback, pattern="^lang_"))
    
    # Oddiy command handler'lar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lang", change_language))
    
    # Message handler'lar
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Botni ishga tushirish
    logger.info("Bot ishga tushirilmoqda...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi (Ctrl+C)")
    except Exception as e:
        logger.error(f"Bot ishga tushirishda xatolik: {e}")

