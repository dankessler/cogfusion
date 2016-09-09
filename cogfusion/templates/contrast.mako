<%inherit file="master.mako"/>


<h1>Contrasts</h1>

        <ul>
% for conceptid in conceptsByContrasts.get(contrast['id'], []):
            <li>${conceptid}</li>
% endfor
        </ul>
