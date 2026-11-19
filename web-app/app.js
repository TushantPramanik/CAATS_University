const $ = (s) => document.querySelector(s);
const authSection = $('#account-section'), workspace = $('#workspace'), wizard = $('#wizard');
let currentUser = null, registerMode = false, wizardStep = 0, answers = {};

const ageBands = ['Under 13', '13–14', '14–15', '15–16', '16–17', '17+'];
const skills = ['Content Creation', 'Video Editing', 'Digital Marketing', 'Entrepreneurship', 'Programming', 'Graphic Designing'];
const masters = ['AI and ML', 'Technical Leadership', 'System Design', 'Fundamentals of Cloud Computing'];
const bsc = ['Physics', 'Mathematics', 'Statistics', 'Economics', 'Computer Science', 'Chemistry', 'Electronics', 'Biotechnology'];
const bca = ['Artificial Intelligence and Machine Learning', 'Cloud Computing', 'Cyber Security', 'Software Development', 'Internet of Things'];
const interests = ['Programming', 'Artificial Intelligence', 'Security & Hacking', 'Data Analysis', 'Electronics', 'Machines & Automobiles', 'Construction & Design', 'Electrical Systems', 'Production', 'Agricultural', 'Food', 'Printing'];

const btech = {
  top: { 'Programming': ['CORE CSE', 'CSE AI/ML', 'CSE Data Science', 'CSE Cyber Security', 'Information Technology', 'CSE IOT'], 'Artificial Intelligence': ['CORE CSE', 'CSE (AI & ML)'], 'Security & Hacking': ['CORE CSE', 'CSE Cyber Security', 'Information Security'], 'Data Analysis': ['CSE Data Science', 'Big Data Analytics', 'CORE CSE'], 'Electronics': ['Electronics & Communication Engineering (ECE)'], 'Machines & Automobiles': ['Mechanical Engineering', 'Automobile Engineering'], 'Construction & Design': ['Civil Engineering'], 'Electrical Systems': ['Electrical Engineering (EE)', 'Electrical & Electronics Engineering (EEE)'] },
  upper: { 'Programming': [], 'Security & Hacking': ['CORE CSE', 'CSE Cyber Security', 'Information Security'], 'Data Analysis': ['CSE Data Science', 'Big Data Analytics', 'CORE CSE'], 'Electronics': ['Electronics & Communication Engineering (ECE)'], 'Machines & Automobiles': ['Mechanical Engineering', 'Automobile Engineering'], 'Construction & Design': ['Civil Engineering'], 'Electrical Systems': ['Electrical Engineering (EE)', 'Electrical & Electronics Engineering (EEE)'] },
  middle: { 'Data Analysis': ['CSE Data Science', 'Big Data Analytics', 'CORE CSE'], 'Electronics': ['Electronics & Communication Engineering (ECE)'], 'Machines & Automobiles': ['Mechanical Engineering', 'Automobile Engineering'], 'Construction & Design': ['Civil Engineering'], 'Electrical Systems': ['Electrical Engineering (EE)', 'Electrical & Electronics Engineering (EEE)'] },
  lower: { 'Electronics': ['Electronics & Communication Engineering (ECE)'], 'Machines & Automobiles': ['Mechanical Engineering', 'Automobile Engineering'], 'Construction & Design': ['Civil Engineering'], 'Electrical Systems': ['Electrical Engineering (EE)', 'Electrical & Electronics Engineering (EEE)'] },
  entry: { 'Machines & Automobiles': ['Mechanical Engineering', 'Automobile Engineering'], 'Construction & Design': ['Civil Engineering'], 'Electrical Systems': ['Electrical Engineering (EE)', 'Electrical & Electronics Engineering (EEE)'], 'Production': ['Production Engineering'], 'Agricultural': ['Agricultural Engineering'] },
  foundation: { 'Agricultural': ['Agricultural Engineering'], 'Food': ['Food Technology'], 'Printing': ['Printing Engineering'] }
};

const EMAIL_REGEX = /^[^@\s]+@[^@\s]+\.[a-zA-Z0-9-]{2,}$/;

function esc(s) {
  return String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function isValidScore(val) {
  if (val === null || val === undefined || val === '') return false;
  const n = Number(val);
  return Number.isFinite(n) && n >= 0 && n <= 100;
}

async function api(url, data) {
  const r = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const j = await r.json();
  if (!r.ok || j.error) throw Error(j.error || 'Please check your inputs and try again.');
  return j;
}

function showAuth() {
  authSection.hidden = false;
  $('#auth-notice').textContent = '';
  $('#auth-form').reset();
  $('#name-wrap').hidden = !registerMode;
  const nameInp = $('#name-wrap input');
  if (nameInp) nameInp.required = registerMode;

  const tabIn = $('#tab-signin');
  const tabReg = $('#tab-register');
  if (tabIn && tabReg) {
    tabIn.classList.toggle('active', !registerMode);
    tabReg.classList.toggle('active', registerMode);
  }

  $('#auth-title').textContent = registerMode ? 'Create your CAATS account' : 'Welcome back';
  $('#auth-sub').textContent = registerMode ? 'Register to save your academic profile and counselling sessions.' : 'Sign in to access your profile and saved recommendations.';
  $('#auth-submit').innerHTML = registerMode ? '<span>Create account</span> <span class="arrow">↗</span>' : '<span>Sign in</span> <span class="arrow">↗</span>';
  $('#switch-copy').textContent = registerMode ? 'Already have an account?' : 'New to CAATS University?';
  $('#switch-auth').textContent = registerMode ? 'Sign in' : 'Create an account';
  $('#auth-form [name=password]').autocomplete = registerMode ? 'new-password' : 'current-password';
}

$('#account-link').onclick = () => currentUser ? workspace.scrollIntoView({ behavior: 'smooth' }) : showAuth();
$('#close-account').onclick = () => authSection.hidden = true;
const authBdrop = $('#auth-backdrop');
if (authBdrop) authBdrop.onclick = () => authSection.hidden = true;

const tabIn = $('#tab-signin');
const tabReg = $('#tab-register');
if (tabIn) tabIn.onclick = () => { registerMode = false; showAuth(); };
if (tabReg) tabReg.onclick = () => { registerMode = true; showAuth(); };

$('#switch-auth').onclick = () => {
  registerMode = !registerMode;
  showAuth();
};

$('#auth-form').onsubmit = async (e) => {
  e.preventDefault();
  const f = new FormData(e.currentTarget);
  const data = Object.fromEntries(f);

  const email = String(data.email || '').trim().toLowerCase();
  const password = String(data.password || '');
  const name = String(data.name || '').trim();

  if (!email || !EMAIL_REGEX.test(email)) {
    $('#auth-notice').textContent = 'Please enter a valid email address (e.g. student@caats.edu).';
    return;
  }

  if (registerMode) {
    if (!name) {
      $('#auth-notice').textContent = 'Please enter your full name.';
      return;
    }
    if (password.length < 8) {
      $('#auth-notice').textContent = 'Password must be at least 8 characters long.';
      return;
    }
  } else {
    if (!password) {
      $('#auth-notice').textContent = 'Please enter your password.';
      return;
    }
  }

  try {
    await api(registerMode ? '/api/register' : '/api/login', { email, password, name });
    authSection.hidden = true;
    await loadMe();
    workspace.scrollIntoView({ behavior: 'smooth' });
  } catch (err) {
    $('#auth-notice').textContent = err.message;
  }
};

$('#logout').onclick = async () => {
  await api('/api/logout', {});
  currentUser = null;
  workspace.hidden = true;
  $('#account-link').innerHTML = '<span class="btn-icon">✦</span> <span class="btn-text">Sign in</span>';
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    if (!wizard.hidden) wizard.hidden = true;
    if (!authSection.hidden) authSection.hidden = true;
  }
});

async function loadMe() {
  const r = await fetch('/api/me');
  const d = await r.json();
  currentUser = d.user;
  if (!currentUser) return;

  authSection.hidden = true;
  workspace.hidden = false;
  const firstName = currentUser.name.split(' ')[0] || 'Student';
  $('#student-name').textContent = firstName;
  const avatar = $('#student-avatar');
  if (avatar) avatar.textContent = (currentUser.name || 'C')[0].toUpperCase();

  $('#account-link').innerHTML = '<span class="btn-icon">✳</span> <span class="btn-text">My Space</span>';
  $('#profile-text').textContent = currentUser.profession ? `${currentUser.profession} · ${currentUser.age_band}` : 'Complete a counselling session to set your profile.';
  $('#history-count').textContent = `${d.history.length} ${d.history.length === 1 ? 'session' : 'sessions'}`;

  const historyEl = $('#history');
  if (d.history.length) {
    historyEl.innerHTML = d.history.map(h => `
      <article class="history-card">
        <div class="history-symbol">✳</div>
        <div class="history-info">
          <small>${esc(h.result.category)}</small>
          <b>${esc(h.result.title)}</b>
          <p>${esc(h.result.detail)}</p>
          ${(h.result.warnings || []).map(w => `<div class="warning">${esc(w)}</div>`).join('')}
        </div>
        <span class="history-date">${new Date(h.created_at + 'Z').toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })}</span>
      </article>
    `).join('');
  } else {
    historyEl.innerHTML = `
      <div class="empty-history-box">
        <div class="empty-icon">✦</div>
        <h4>No counselling sessions yet</h4>
        <p>Start your first guided session to discover your eligible degree branches, subjects, and skill tracks.</p>
        <button class="button primary small" id="empty-start-btn" type="button">
          <span>Start your first session</span>
          <span class="arrow">↗</span>
        </button>
      </div>
    `;
    const emptyBtn = $('#empty-start-btn');
    if (emptyBtn) emptyBtn.onclick = openWizard;
  }
}

function openWizard() {
  if (!currentUser) {
    registerMode = false;
    showAuth();
    return;
  }
  answers = {};
  wizardStep = 0;
  $('#wizard-notice').textContent = '';
  wizard.hidden = false;
  renderStep();
}

$('#start-btn').onclick = openWizard;
$('#start-bottom').onclick = openWizard;
$('#workspace-start').onclick = openWizard;
$('#wizard-close').onclick = () => wizard.hidden = true;
const wizBdrop = $('#wizard-backdrop');
if (wizBdrop) wizBdrop.onclick = () => wizard.hidden = true;

function cardGroup(key, items) {
  return `<div class="field-grid">${items.map(x => `
    <label class="choice">
      <input type="radio" name="${key}" value="${esc(x)}" ${answers[key] === x ? 'checked' : ''}>
      <span>${esc(x)}</span>
    </label>
  `).join('')}</div>`;
}

function fieldNumber(key, label) {
  const currentVal = answers[key] ?? '';
  return `
    <label class="text-field">${label}
      <input name="${key}" type="number" min="0" max="100" step="any" value="${esc(currentVal)}" placeholder="Enter a score from 0 to 100">
    </label>
  `;
}

function stageTitle() {
  if (wizardStep === 0) return ['A little about you', 'Your journey begins with where you are today.'];
  if (wizardStep === 1) return ['Choose your direction', 'What pathway would you like to explore?'];
  return ['Let’s find your fit', 'Select the option that aligns with your goals.'];
}

function buildStages() {
  if (wizardStep === 0) {
    return `
      <h2 id="wizard-title">${stageTitle()[0]}</h2>
      <p class="lead">${stageTitle()[1]}</p>
      <div class="field-caption">I am a</div>
      ${cardGroup('profession', ['Student', 'Working', 'Other'])}
      <div class="field-caption">My age group</div>
      ${cardGroup('age_band', ageBands)}
    `;
  }

  if (wizardStep === 1) {
    let paths = answers.profession === 'Working'
      ? ['Skills', '4-hour master class']
      : answers.profession === 'Other'
        ? ['Skills']
        : answers.age_band === 'Under 13'
          ? ['Skills']
          : answers.age_band === '17+'
            ? ['College', 'Skills']
            : ['School', 'Skills'];

    return `
      <h2 id="wizard-title">${stageTitle()[0]}</h2>
      <p class="lead">${stageTitle()[1]}</p>
      ${cardGroup('pathway', paths)}
    `;
  }

  if (answers.pathway === 'Skills' || answers.profession === 'Other') {
    return `
      <h2 id="wizard-title">Build a skill track</h2>
      <p class="lead">Pick a specialized area you would like to develop.</p>
      ${cardGroup('choice', skills)}
    `;
  }

  if (answers.pathway === '4-hour master class') {
    return `
      <h2 id="wizard-title">Choose an executive master class</h2>
      <p class="lead">Each focused master class is four hours, exactly as offered in the original project.</p>
      ${cardGroup('choice', masters)}
    `;
  }

  if (answers.pathway === 'School') {
    return `
      <h2 id="wizard-title">Pick your academic focus</h2>
      <p class="lead">Your age band maps directly to your school class in the original project.</p>
      ${cardGroup('choice', ['Boards', 'Olympiad'])}
    `;
  }

  if (wizardStep === 2) {
    const rawP = answers.percentage;
    let feedback = '';
    if (rawP !== null && rawP !== undefined && rawP !== '') {
      const pNum = Number(rawP);
      if (!Number.isFinite(pNum) || pNum < 0 || pNum > 100) {
        feedback = '<div class="warning">Percentage must be a valid number between 0 and 100. Values outside 0–100 are not accepted.</div>';
      } else if (pNum < 33) {
        feedback = '<div class="warning">Below 33%, the source project indicates that college admission is not possible. Continue to save this result with your session.</div>';
      }
    }

    const options = collegeOptions();
    return `
      <h2 id="wizard-title">Choose your college pathway</h2>
      <p class="lead">Your Class 12 percentage determines which degree courses the university offers.</p>
      ${fieldNumber('percentage', 'Class 12 percentage (0 to 100)')}
      ${feedback}
      <div id="college-options">
        ${options.length ? cardGroup('course', options) : ''}
      </div>
    `;
  }

  if (answers.course === 'Diploma' && wizardStep === 3) {
    return `
      <h2 id="wizard-title">Diploma / Polytechnic pathway</h2>
      <p class="lead">The original diploma rules were not in the uploaded files. You can save this selection as a pathway note.</p>
      <div class="result-box">
        <small style="letter-spacing:1px;color:var(--primary);font-weight:700;">COURSE SELECTED</small>
        <h3 style="margin:8px 0 0;font:600 20px var(--serif);">Diploma Engineering Track</h3>
        <div class="warning" style="margin-top:14px;">The referenced K_diploma_clg_dep.py module was not included in the initial upload. Choosing this saves your pathway preference and notes the rule gap.</div>
      </div>
    `;
  }

  if (answers.course === 'BTech' && wizardStep === 3) {
    const rawJ = answers.jee;
    let feedback = '';
    const avail = availableInterests();

    if (rawJ === null || rawJ === undefined || rawJ === '') {
      feedback = '<div class="hint">✦ Enter your CAATS JEE percentile above to see available interest areas.</div>';
    } else {
      const jNum = Number(rawJ);
      if (!Number.isFinite(jNum) || jNum < 0 || jNum > 100) {
        feedback = '<div class="warning">CAATS JEE percentile must be a valid number between 0 and 100.</div>';
      } else if (!avail.length) {
        feedback = '<div class="warning">The source project defines no BTech branches for this percentile range. Continue to save this rule gap with your session.</div>';
      }
    }

    return `
      <h2 id="wizard-title">What interests you?</h2>
      <p class="lead">Available options depend on the CAATS JEE percentile band in the original project.</p>
      ${fieldNumber('jee', 'CAATS JEE percentile (0 to 100)')}
      <div id="interest-options">
        ${feedback}
        ${avail.length ? cardGroup('interest', avail) : ''}
      </div>
    `;
  }

  if (answers.course === 'BTech') {
    const b = band(answers.jee);
    let list = (btech[b] || {})[answers.interest] || [];

    let note = '';
    if (b === 'upper' && answers.interest === 'Programming') {
      note = '<div class="warning">Programming is listed as an interest for 75–84 in the source, but its BTech branch-choice block is missing. Return to select another interest or continue to document this rule gap.</div>';
    } else if (!list.length) {
      note = '<div class="warning">The uploaded source does not define a branch choice for this combination. Continue to save this rule gap with your session.</div>';
    }

    return `
      <h2 id="wizard-title">Choose your specialization</h2>
      <p class="lead">Based on your score and interest in <strong>${esc(answers.interest || 'None selected')}</strong>.</p>
      ${note}
      ${list.length ? cardGroup('choice', list) : ''}
    `;
  }

  // BSc or BCA choices
  const options = courseOptions();
  let bscNote = '';
  if (answers.course === 'BSc' && Number(answers.percentage) === 40) {
    bscNote = '<div class="warning">At exactly 40%, the source branches conflict: a >=40 tier offers Biotechnology, while a later <=40 condition says not eligible. The site follows Biotechnology with this warning.</div>';
  } else if (answers.course === 'BCA' && Number(answers.percentage) >= 70 && Number(answers.percentage) < 75) {
    bscNote = '<div class="warning">The BCA source does not define recommendations for 70% to below 75%. Continue to save this rule gap with your session.</div>';
  } else if (!options.length) {
    bscNote = '<div class="warning">The uploaded source has no options defined for this percentage range. Continue to save this rule gap with your session.</div>';
  }

  return `
    <h2 id="wizard-title">Choose your ${esc(answers.course)} path</h2>
    <p class="lead">Options reflect the percentage bands in the uploaded source.</p>
    ${bscNote}
    ${options.length ? cardGroup('choice', options) : ''}
  `;
}

function band(v) {
  if (v === null || v === undefined || v === '') return 'none';
  const n = Number(v);
  if (!Number.isFinite(n) || n < 0 || n > 100) return 'none';
  return n >= 85 ? 'top' : n >= 75 && n <= 84 ? 'upper' : n >= 65 && n <= 74 ? 'middle' : n >= 55 && n <= 64 ? 'lower' : n >= 45 && n <= 54 ? 'entry' : n >= 35 && n <= 44 ? 'foundation' : 'none';
}

function availableInterests() {
  const b = band(answers.jee);
  return Object.keys(btech[b] || {});
}

function collegeOptions() {
  if (answers.percentage === null || answers.percentage === undefined || answers.percentage === '') {
    return ['BTech', 'BSc', 'BCA', 'Diploma'];
  }
  const p = Number(answers.percentage);
  if (!Number.isFinite(p) || p < 0 || p > 100) return [];
  if (p >= 75) return ['BTech', 'BSc', 'BCA', 'Diploma'];
  if (p >= 55) return ['BSc', 'BCA', 'Diploma'];
  if (p >= 40) return ['BSc', 'Diploma'];
  if (p >= 33) return ['Diploma'];
  return [];
}

function courseOptions() {
  if (!isValidScore(answers.percentage)) return [];
  const p = Number(answers.percentage);

  if (answers.course === 'BSc') {
    if (p >= 75) return bsc;
    if (p >= 70) return bsc.slice(1);
    if (p >= 65) return bsc.slice(2);
    if (p >= 60) return bsc.slice(3);
    if (p >= 55) return bsc.slice(4);
    if (p > 40) return bsc.slice(6);
    if (p === 40) return ['Biotechnology'];
    return [];
  }

  if (answers.course === 'BCA') {
    if (p >= 80) return bca;
    if (p >= 75) return bca.slice(1);
    if (p >= 65 && p < 70) return bca.slice(2);
    if (p >= 60 && p < 65) return bca.slice(3);
    if (p >= 55 && p < 60) return bca.slice(4);
    return [];
  }

  return [];
}

function renderStep() {
  const max = maxStage();
  $('#wizard-content').innerHTML = buildStages();
  $('#progress-fill').style.width = `${Math.min(100, Math.round(100 * (wizardStep + 1) / (max + 1)))}%`;
  $('#step-count').textContent = `STEP ${wizardStep + 1} OF ${max + 1}`;
  $('#wizard-back').hidden = wizardStep === 0;
  $('#wizard-next').innerHTML = wizardStep === max ? '<span>Save my result</span> <span class="arrow">↗</span>' : '<span>Continue</span> <span class="arrow">→</span>';

  // Live input handler for CAATS JEE Percentile
  const jee = $('#wizard-content [name=jee]');
  if (jee) {
    jee.oninput = () => {
      answers.jee = jee.value.trim() === '' ? null : jee.value.trim();
      const box = $('#interest-options');
      if (box) {
        const raw = answers.jee;
        let feedback = '';
        const avail = availableInterests();

        if (raw === null || raw === undefined || raw === '') {
          feedback = '<div class="hint">✦ Enter your CAATS JEE percentile above to see available interest areas.</div>';
        } else {
          const n = Number(raw);
          if (!Number.isFinite(n) || n < 0 || n > 100) {
            feedback = '<div class="warning">CAATS JEE percentile must be a valid number between 0 and 100.</div>';
          } else if (!avail.length) {
            feedback = '<div class="warning">The source project defines no BTech branches for this percentile range. Continue to save this rule gap with your session.</div>';
          }
        }

        box.innerHTML = `${feedback}${avail.length ? cardGroup('interest', avail) : ''}`;
      }
    };
  }

  // Live input handler for Class 12 Percentage
  const percent = $('#wizard-content [name=percentage]');
  if (percent) {
    percent.oninput = () => {
      answers.percentage = percent.value.trim() === '' ? null : percent.value.trim();
      const box = $('#college-options');
      const options = collegeOptions();
      const raw = answers.percentage;

      let feedback = '';
      if (raw !== null && raw !== undefined && raw !== '') {
        const n = Number(raw);
        if (!Number.isFinite(n) || n < 0 || n > 100) {
          feedback = '<div class="warning">Percentage must be a valid number between 0 and 100. Values outside 0–100 are not accepted.</div>';
        } else if (n < 33) {
          feedback = '<div class="warning">Below 33%, the source project indicates that college admission is not possible. Continue to save this result with your session.</div>';
        }
      }

      if (box) {
        box.innerHTML = `${feedback}${options.length ? cardGroup('course', options) : ''}`;
      }
      if (!options.includes(answers.course)) {
        answers.course = null;
      }
    };
  }
}

function collect() {
  document.querySelectorAll('#wizard-content input[type=radio]:checked, #wizard-content input[type=number], #wizard-content select').forEach(el => {
    if (el.type === 'number') {
      answers[el.name] = el.value.trim() === '' ? null : el.value.trim();
    } else {
      answers[el.name] = el.value;
    }
  });

  if (wizardStep === 0 && answers.profession && answers.age_band) {
    if (answers.profession === 'Working' && answers.age_band === '17+') answers.pathway ||= 'Skills';
    else if (answers.profession === 'Other') answers.pathway = 'Skills';
    else if (answers.profession === 'Student') answers.pathway = answers.age_band === 'Under 13' ? 'Skills' : answers.age_band === '17+' ? 'College' : 'School';
  }

  if (wizardStep === 1) {
    const val = document.querySelector('#wizard-content input[name=pathway]:checked')?.value;
    if (val) answers.pathway = val;
    answers.choice = null;
    answers.course = null;
    answers.interest = null;
  }

  if (wizardStep === 2 && answers.course === 'BTech') {
    const val = document.querySelector('#wizard-content input[name=interest]:checked')?.value;
    if (val) answers.interest = val;
  }
}

function validateCurrentStep() {
  if (wizardStep === 0) {
    if (!answers.profession || !answers.age_band) {
      $('#wizard-notice').textContent = 'Please select both your profession and age group to continue.';
      return false;
    }
    if (answers.profession === 'Working' && answers.age_band !== '17+') {
      $('#wizard-notice').textContent = 'The source project limits the work pathway to age 17+.';
      return false;
    }
    return true;
  }

  if (wizardStep === 1) {
    if (!answers.pathway) {
      $('#wizard-notice').textContent = 'Please choose a pathway to explore.';
      return false;
    }
    return true;
  }

  // Skills / Master / School
  if (answers.pathway === 'Skills' || answers.profession === 'Other' || answers.pathway === '4-hour master class' || answers.pathway === 'School') {
    if (!answers.choice) {
      $('#wizard-notice').textContent = 'Please select an option from the list above.';
      return false;
    }
    return true;
  }

  // Step 2: College course selection & percentage
  if (wizardStep === 2) {
    if (answers.percentage === null || answers.percentage === undefined || answers.percentage === '') {
      $('#wizard-notice').textContent = 'Please enter your Class 12 percentage.';
      return false;
    }
    const p = Number(answers.percentage);
    if (!Number.isFinite(p) || p < 0 || p > 100) {
      $('#wizard-notice').textContent = 'Class 12 percentage must be a valid number between 0 and 100.';
      return false;
    }
    if (p < 33) {
      // Below 33%, college admission not possible in source; can proceed to save rule result
      return true;
    }
    if (!answers.course) {
      $('#wizard-notice').textContent = 'Please select an eligible degree course to continue.';
      return false;
    }
    return true;
  }

  // Step 3: Diploma note
  if (answers.course === 'Diploma') {
    return true;
  }

  // Step 3: BTech CAATS JEE percentile
  if (answers.course === 'BTech' && wizardStep === 3) {
    if (answers.jee === null || answers.jee === undefined || answers.jee === '') {
      $('#wizard-notice').textContent = 'Please enter your CAATS JEE percentile.';
      return false;
    }
    const j = Number(answers.jee);
    if (!Number.isFinite(j) || j < 0 || j > 100) {
      $('#wizard-notice').textContent = 'CAATS JEE percentile must be a valid number between 0 and 100.';
      return false;
    }
    const b = band(j);
    if (b === 'none') {
      // Uncovered band; user can continue to save the rule gap
      return true;
    }
    if (!answers.interest) {
      $('#wizard-notice').textContent = 'Please choose an area of interest for your score band.';
      return false;
    }
    return true;
  }

  // Step 4: BTech Branch choice
  if (answers.course === 'BTech') {
    const b = band(answers.jee);
    const list = (btech[b] || {})[answers.interest] || [];
    if (!list.length) {
      // Missing choice block (e.g. Programming at 75-84) or uncovered gap; allow continue to record gap
      return true;
    }
    if (!answers.choice) {
      $('#wizard-notice').textContent = 'Please select a specialization branch.';
      return false;
    }
    return true;
  }

  // Step 3: BSc or BCA branch choice
  if (answers.course === 'BSc' || answers.course === 'BCA') {
    const options = courseOptions();
    if (!options.length) {
      // Gap tier (e.g. BCA 70-75%); allow continue to save rule gap
      return true;
    }
    if (!answers.choice) {
      $('#wizard-notice').textContent = `Please select a ${answers.course} specialization.`;
      return false;
    }
    return true;
  }

  return true;
}

function maxStage() {
  if (answers.percentage !== null && answers.percentage !== undefined && answers.percentage !== '') {
    const p = Number(answers.percentage);
    if (Number.isFinite(p) && p < 33 && p >= 0) return 2;
  }
  return answers.pathway === 'College' && answers.course === 'BTech' ? 4 : answers.pathway === 'College' && answers.course ? 3 : 2;
}

function showResult(result) {
  $('#wizard-kicker').textContent = 'A STARTING POINT FOR YOUR JOURNEY';
  $('#progress-fill').style.width = '100%';
  $('#step-count').textContent = 'COMPLETED';
  $('#wizard-content').innerHTML = `
    <div class="result-box">
      <div class="result-mark">✳</div>
      <div class="result-category">${esc(result.category)}</div>
      <h2 class="result-title">${esc(result.title)}</h2>
      <p class="result-detail">${esc(result.detail || '')}</p>
      ${(result.warnings || []).map(x => `<div class="warning">${esc(x)}</div>`).join('')}
    </div>
    <p class="lead" style="margin-top:16px">This personalized starting point is saved to your student profile space.</p>
  `;
  $('#wizard-back').hidden = true;
  $('#wizard-next').innerHTML = '<span>View in my space</span> <span class="arrow">✓</span>';
  $('#wizard-next').onclick = () => {
    wizard.hidden = true;
    $('#wizard-next').onclick = nextStep;
    loadMe();
    workspace.scrollIntoView({ behavior: 'smooth' });
  };
}

async function nextStep() {
  if ($('#wizard-next').textContent.includes('✓')) return;
  collect();
  $('#wizard-notice').textContent = '';

  if (!validateCurrentStep()) {
    return;
  }

  if (wizardStep < maxStage()) {
    wizardStep++;
    renderStep();
    return;
  }

  // Parse numeric scores for API submission
  const finalPercentage = answers.percentage !== null && answers.percentage !== undefined && answers.percentage !== ''
    ? Number(answers.percentage)
    : null;

  const finalJee = answers.jee !== null && answers.jee !== undefined && answers.jee !== ''
    ? Number(answers.jee)
    : null;

  try {
    const result = await api('/api/recommend', {
      answers: {
        ...answers,
        profession: answers.profession,
        age_band: answers.age_band,
        pathway: answers.pathway === '4-hour master class' ? 'master' : answers.pathway === 'School' ? 'school' : answers.pathway === 'College' ? 'college' : answers.pathway === 'Skills' ? 'skills' : answers.pathway?.toLowerCase(),
        percentage: finalPercentage,
        jee: finalJee
      }
    });
    showResult(result.result);
  } catch (err) {
    $('#wizard-notice').textContent = err.message;
  }
}

$('#wizard-next').onclick = nextStep;
$('#wizard-back').onclick = () => {
  collect();
  wizardStep = Math.max(0, wizardStep - 1);
  renderStep();
};

async function boot() {
  await loadMe();
  if (!currentUser) workspace.hidden = true;
}

boot();
