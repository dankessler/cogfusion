<%inherit file="master.mako"/>


<h1>Contrasts</h1>

<ul>
% for index, contrast in contrasts.iterrows():
    <li>
        <a href="${request.route_url('contrasts',contrast['id'])}">${contrast['contrast_text']}</a>
    </li>
% endfor
</ul>



