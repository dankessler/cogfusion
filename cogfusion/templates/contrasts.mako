<%inherit file="master.mako"/>


<h1>Contrasts</h1>

<ul>
% for index, contrast in contrasts.iterrows():
    <li>
        ${contrast['contrast_text']}
        <ul>
% for conceptid in conceptsByContrasts.get(contrast['id'], []):
            <li>${conceptid}</li>
% endfor
        </ul>
    </li>
% endfor
</ul>



